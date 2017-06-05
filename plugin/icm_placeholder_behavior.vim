
" Placeholder Logic

function! GetPlaceholderPattern()
    return '<#\%(T##\)\?\%([^#]\+##\)\?\([^#]\+\)#>'
endfunction

function! JumpToPlaceholder()
    if &filetype !=# 'swift'
        return 0
    end

    if !CheckPlaceholderExistence()
        return 0
    endif

    call BeginReplacingPlaceholder()
    return 1
endfunction

function! BeginReplacingPlaceholder()
    let l:pattern = GetPlaceholderPattern()
    let [l:line, l:column] = searchpos(l:pattern)
    if l:line == 0 && l:column == 0
        return
    end
    execute printf(':%d s/%s//', l:line, l:pattern)
    call cursor(l:line, l:column)
endfunction

function! CheckPlaceholderExistence()
    " Go to the first instance of the placeholder
    return search(GetPlaceholderPattern(), 'b')
endfunction


" Events

let s:loglevel = 0

function! s:DebugEcho(msg)
    if s:loglevel
         echom a:msg
    endif
endfunction


function! s:OnTextChangedInsertMode()
    call s:DebugEcho("OnTextChangedInsertMode")
    if pumvisible()
        call s:DebugEcho("pumvisible()")
    endif

    let s:behaviorstate = 1
endfunction

" User behavior is tracked through the `behaviorstate` state machine. We
" listen to events to know when to jump between placeholders.
"
" 0: Clear
" User typing states
" 1: Will start typing text
" 2: Did end typing text
" 3: Did tab with out pumvisible()
" 4: Did tab with pumvisible()
" Jump states:
" 11: Triggered a jump CompleteDone
" 13: Triggered a jump for InsertLeave
let s:behaviorstate = 0

fun! s:OnTextChangedI()
    call s:DebugEcho("OnTextChangedI")
    if s:behaviorstate == 1
          let s:behaviorstate = 2
    endif
endf

function! s:OnInsertCharPre()
    call s:DebugEcho("OnInsertCharPre")
    if s:behaviorstate == 0
        return
    end
    if s:behaviorstate == 11
        call s:DebugEcho("OnInsertCharPre.AfterOnCompleteDone")
    end
endfunction


function! s:OnInsertLeave()
    call s:DebugEcho("OnInsertLeave")
    if s:behaviorstate == 3
        call s:DebugEcho("OnInsertLeave.Check")
        if s:InsideUnclosedStringLiteralParameter() == 0
            call s:DebugEcho("OnInsertLeave.WillJump")
            call JumpToPlaceholder()
            let s:behaviorstate = 13
        else
            call cursor( line('.'), col('.') + 1)
        endif
        startinsert
    end
    let s:behaviorstate = 0
endfunction

" After completion - jump to the next placeholder
" Do this once per event to prevent eargerly jumping
" between placholders
function! s:OnCompleteDone()
    call s:DebugEcho("OnCompleteDone")
    if s:behaviorstate == 2 || s:behaviorstate == 4
        call s:DebugEcho("OnCompleteDone.Invoke")
        if JumpToPlaceholder()
            call s:DebugEcho("OnCompleteDone.DidJump")
            let s:behaviorstate = 11
        end
        return
    endif
endfunction

" Test if the user is inside of an unclosed string literal
" parameter.
"
" Examples:
" some(foo: '
" will return 1
"
" some(foo: ' '
" will return 0
function! s:InsideUnclosedStringLiteralParameter()
    let line = getline(".")
    let col  = col(".")
    let offset = col
    " Test if there is an opening character before the current position
    let openingQuote = ""
    while offset > 0
        let value = matchstr(line, '\%' . offset . 'c.')
        if value == "\"" || value == "'"
            let prevVal = line[offset - 2]
            if prevVal != "\\"
                let openingQuote = value
                break
            endif
         endif
         let offset = offset - 1
    endwhile
    if openingQuote == ""
        return 0
    endif

    " Now, search forward from the users position
    " to see if there is a string.
    " Loop to the end of the line for simplicity.
    let offset = col
    let closingQuote = ""
    let linelen = strlen(line)
    while offset < linelen
       let value = matchstr(line, '\%' . offset . 'c.')
       if value == openingQuote
           let prevVal = line[offset - 2]
           if prevVal != "\\"
                 let closingQuote = value
                 break
           endif
       endif
       let offset = offset + 1
    endwhile

    " If there isn't a closing quote, then we are in an unclosed literal
    return closingQuote == ""
endfunction

" Override the tab callback.
" When the user tabs, we check if completion has ended
" and if so, then jump to the next
" This forces '<Tab>' and '<Down>', which seems sensible
" TODO:jerry consider how this will manifest in the user level
" and a way to overide it.
let g:icm_key_list_select_completion = ['<Down>']

function! DidTab()
    call s:DebugEcho("DidTab")
    if pumvisible()
        let s:behaviorstate = 4
        " Make the tab key work like how it used to in iCM
        " when the pum is visible, we'll go to the next value.
        " FIXME: This needs some smarts before merging.
        " If the user is typing a string with a tab in it, it will be
        " problematic.
        return "\<C-n>"
    else
        if CheckPlaceholderExistence()
           " Exit insert mode for a flash :)
           " In a few clicks, when InsertLeave event is received, we'll reenter
           " it again.
           call s:DebugEcho("DidTab.HasPlaceholder")
           let s:behaviorstate = 3
           return "\<esc>"
        endif
        return "\<tab>"
    endif
endfunction

" Key Mappings

" TODO:jerry Don't use noremap ( iCM ) uses this too
" Perhaps this can be a custom value
" This takes precedence ( but is kind of sketchy )
inoremap <expr> <tab> DidTab()
nmap <C-k> :call JumpToPlaceholder() <CR>

" Bootstrap autocommands
" TODO:jerry
" - scope to swift and disable debugging
" - improve loading ( maybe autoload or something ? )
autocmd CompleteDone * call s:OnCompleteDone()
autocmd InsertCharPre * call s:OnInsertCharPre()
autocmd TextChangedI * call s:OnTextChangedI()
autocmd InsertLeave * call s:OnInsertLeave()

