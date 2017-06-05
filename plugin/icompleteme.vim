" Copyright (C) 2011, 2012  Google Inc.
"
" This file is part of iCompleteMe.
"
" iCompleteMe is free software: you can redistribute it and/or modify
" it under the terms of the GNU General Public License as published by
" the Free Software Foundation, either version 3 of the License, or
" (at your option) any later version.
"
" iCompleteMe is distributed in the hope that it will be useful,
" but WITHOUT ANY WARRANTY; without even the implied warranty of
" MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
" GNU General Public License for more details.
"
" You should have received a copy of the GNU General Public License
" along with iCompleteMe.  If not, see <http://www.gnu.org/licenses/>.

" This is basic vim plugin boilerplate
let s:save_cpo = &cpo
set cpo&vim

function! s:restore_cpo()
  let &cpo = s:save_cpo
  unlet s:save_cpo
endfunction
if exists( "g:loaded_icompleteme" )
  call s:restore_cpo()
  finish
elseif v:version < 704 || (v:version == 704 && !has( 'patch1578' ))
  echohl WarningMsg |
        \ echomsg "iCompleteMe unavailable: requires Vim 7.4.1578+" |
        \ echohl None
  call s:restore_cpo()
  finish
elseif !has( 'timers' )
  echohl WarningMsg |
        \ echomsg "iCompleteMe unavailable: requires Vim compiled with " .
        \ "the timers feature" |
        \ echohl None
  call s:restore_cpo()
  finish
elseif !has( 'python' ) && !has( 'python3' )
  echohl WarningMsg |
        \ echomsg "iCompleteMe unavailable: requires Vim compiled with " .
        \ "Python (2.6+ or 3.3+) support" |
        \ echohl None
  call s:restore_cpo()
  finish
endif

let g:loaded_icompleteme = 1

" NOTE: Most defaults are in third_party/ycmd/ycmd/default_settings.json. They
" are loaded into Vim globals with the 'icm_' prefix if such a key does not
" already exist; thus, the user can override the defaults.
" The only defaults that are here are the ones that are only relevant to the YCM
" Vim client and not the ycmd server.

let g:icm_open_loclist_on_icm_diags =
      \ get( g:, 'icm_open_loclist_on_icm_diags', 1 )

let g:icm_add_preview_to_completeopt =
      \ get( g:, 'icm_add_preview_to_completeopt', 0 )

let g:icm_autoclose_preview_window_after_completion =
      \ get( g:, 'icm_autoclose_preview_window_after_completion', 0 )

let g:icm_autoclose_preview_window_after_insertion =
      \ get( g:, 'icm_autoclose_preview_window_after_insertion', 0 )

let g:icm_key_list_select_completion =
      \ get( g:, 'icm_key_list_select_completion', ['<TAB>', '<Down>'] )

let g:icm_key_list_previous_completion =
      \ get( g:, 'icm_key_list_previous_completion', ['<S-TAB>', '<Up>'] )

let g:icm_key_invoke_completion =
      \ get( g:, 'icm_key_invoke_completion', '<C-Space>' )

let g:icm_key_detailed_diagnostics =
      \ get( g:, 'icm_key_detailed_diagnostics', '<leader>d' )

let g:icm_cache_omnifunc =
      \ get( g:, 'icm_cache_omnifunc', 1 )

let g:icm_log_level =
      \ get( g:, 'icm_log_level',
      \ get( g:, 'icm_server_log_level', 'info' ) )

let g:icm_keep_logfiles =
      \ get( g:, 'icm_keep_logfiles',
      \ get( g:, 'icm_server_keep_logfiles', 0 ) )

let g:icm_extra_conf_vim_data =
      \ get( g:, 'icm_extra_conf_vim_data', [] )

let g:icm_server_python_interpreter =
      \ get( g:, 'icm_server_python_interpreter',
      \ get( g:, 'icm_path_to_python_interpreter', '' ) )

let g:icm_show_diagnostics_ui =
      \ get( g:, 'icm_show_diagnostics_ui', 1 )

let g:icm_enable_diagnostic_signs =
      \ get( g:, 'icm_enable_diagnostic_signs',
      \ get( g:, 'syntastic_enable_signs', 1 ) )

let g:icm_enable_diagnostic_highlighting =
      \ get( g:, 'icm_enable_diagnostic_highlighting',
      \ get( g:, 'syntastic_enable_highlighting', 1 ) )

let g:icm_echo_current_diagnostic =
      \ get( g:, 'icm_echo_current_diagnostic',
      \ get( g:, 'syntastic_echo_current_error', 1 ) )

let g:icm_always_populate_location_list =
      \ get( g:, 'icm_always_populate_location_list',
      \ get( g:, 'syntastic_always_populate_loc_list', 0 ) )

let g:icm_error_symbol =
      \ get( g:, 'icm_error_symbol',
      \ get( g:, 'syntastic_error_symbol', '>>' ) )

let g:icm_warning_symbol =
      \ get( g:, 'icm_warning_symbol',
      \ get( g:, 'syntastic_warning_symbol', '>>' ) )

let g:icm_goto_buffer_command =
      \ get( g:, 'icm_goto_buffer_command', 'same-buffer' )

let g:icm_disable_for_files_larger_than_kb =
      \ get( g:, 'icm_disable_for_files_larger_than_kb', 1000 )

if has( 'vim_starting' ) " Loading at startup.
  " We defer loading until after VimEnter to allow the gui to fork (see
  " `:h gui-fork`) and avoid a deadlock situation, as explained here:
  " https://github.com/Valloric/iCompleteMe/pull/2473#issuecomment-267716136
  augroup icompletemeStart
    autocmd!
    autocmd VimEnter * call icompleteme#Enable()
  augroup END
else " Manual loading with :packadd.
  call icompleteme#Enable()
endif

" This is basic vim plugin boilerplate
call s:restore_cpo()

" Vim does not support Swift right now
autocmd BufNewFile,BufRead *.swift set filetype=swift

" Disable ycm for swift
let g:ycm_filetype_blacklist = { "swift" : 1 }

