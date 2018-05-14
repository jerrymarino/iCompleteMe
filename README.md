iCompleteMe: Swift comprehension in Vim
===============================================

[![Build Status](https://travis-ci.org/jerrymarino/iCompleteMe.svg?branch=master)](https://travis-ci.org/jerrymarino/iCompleteMe)
[![Build status](https://ci.appveyor.com/api/projects/status/ag9uqwi8s6btwjd8/branch/master?svg=true)](https://ci.appveyor.com/project/jerrymarino/iCompleteMe)

- [Intro](#intro)
- [Background](#background)
- [Installation](#installation)
    - [Mac OS X](#mac-os-x)
    - [Ubuntu Linux x64](#ubuntu-linux-x64)
    - [Fedora Linux x64](#fedora-linux-x64)
    - [Windows](#windows)
    - [FreeBSD/OpenBSD](#freebsdopenbsd)
    - [Full Installation Guide](#full-installation-guide)
- [Quick Feature Summary](#quick-feature-summary)
- [User Guide](#user-guide)
    - [General Usage](#general-usage)
    - [Client-Server Architecture](#client-server-architecture)
    - [Completion String Ranking](#completion-string-ranking)
    - [General Semantic Completion](#general-semantic-completion)
    - [Diagnostic Display](#diagnostic-display)
        - [Diagnostic Highlighting Groups](#diagnostic-highlighting-groups)
- [Functions](#functions)
- [Autocommands](#autocommands)
- [Options](#options)
- [FAQ](#faq)
- [Contributor Code of Conduct](#contributor-code-of-conduct)
- [Contact](#contact)
- [License](#license)

Intro
-----

### Featuring

* Semantic completion
* Semantic Diagnostics: see real-time warnings and errors before builds
* Super-fast identifier completer including tags files and syntax elements
* Swifty placeholder navigation: tab swiftly through long method completions

![SwiftySwiftVimPreview](https://cloud.githubusercontent.com/assets/1245820/26759463/4084bde8-48b3-11e7-869b-33ec00d70eef.gif)


*Warning: it's in a bleeding edge, pre-alpha state.*


Background
-----

[iCompleteMe][] is based on [YouCompleteMe][]. After spending a over a year
attempting to implement Swift support for [YouCompleteMe][], I found that it
wasn't possible to achieve ideal behavior under the conventions of [YCM][];
[iCM][] spawned.

Instead of shoehorning Swift into completion behaviors that work OK for other
languages, [iCompleteMe][] implements behaviors which are ideal for Swift.

Additionally, [iCompleteMe][]'s core subsystems only work with Swift.  The
codebase has a significantly smaller footprint, which makes it easier to
install, easier to reason about, and more stable on the CI ( in theory ).

The name [iCompleteMe][] is a statement about developing a system that
considers ideal behaviors for an *individual* language and a tribute to
[Valloric][]'s and the [YCM][]'s teams legacy.

** It can exist in parallel to [YouCompleteMe][]: use [iCompleteMe][] for the
Swift files.**

Installation
------------

### Mac OS X

These instructions (using `install.py`) are the quickest way to install
iCompleteMe, however they may not work for everyone. If the following
instructions don't work for you, check out the [full installation
guide](#full-installation-guide).

Install the latest version of [MacVim][]. Yes, MacVim. And yes, the _latest_.

If you don't use the MacVim GUI, it is recommended to use the Vim binary that is
inside the MacVim.app package (`MacVim.app/Contents/MacOS/Vim`). To ensure it
works correctly copy the `mvim` script from the [MacVim][] download to your
local binary folder (for example `/usr/local/bin/mvim`) and then symlink it:

    ln -s /usr/local/bin/mvim vim

Install iCompleteMe with [Vundle][].

**Remember:** iCM is a plugin with a compiled component. If you **update** iCM
using Vundle and the ycm_core library APIs have changed (happens
rarely), iCM will notify you to recompile it. You should then rerun the install
process.

**NOTE:** If you want Swift completion, you MUST have the latest Xcode
installed along with the latest Command Line Tools (they are installed
automatically when you run `clang` for the first time, or manually by running
`xcode-select --install`)

Install CMake. Preferably with [Homebrew][brew], but here's the [stand-alone
CMake installer][cmake-download].

_If_ you have installed a Homebrew Python and/or Homebrew MacVim, see the _FAQ_
for details.

Simply run:

    cd ~/.vim/bundle/iCompleteMe
    ./install.py

That's it. You're done. Refer to the _User Guide_ section on how to use iCM.
Don't forget that if you want the Swift semantic completion engine to work,
you will need to provide the compilation flags for your project to iCM. It's all
in the User Guide.

iCM comes with sane defaults for its options, but you still may want to take a
look at what's available for configuration. There are a few interesting options
that are conservatively turned off by default that you may want to turn on.

**iCM Relies on [SwiftySwiftVim][] for language support. By default, it links
libraries from Xcode ( using whatever Xcode `xcode-select` points at ). If
you'd like to build from source, checkout [SwiftySwiftVim][]'s build system for
more info**

### Ubuntu Linux x64

Untested: Requires building [SwiftySwiftVim][] from source.

These instructions (using `install.py`) are the quickest way to install
iCompleteMe, however they may not work for everyone. If the following
instructions don't work for you, check out the [full installation
guide](#full-installation-guide).

Make sure you have Vim 7.4.1578 with Python 2 or Python 3 support. Ubuntu 16.04
and later have a Vim that's recent enough. You can see the version of Vim
installed by running `vim --version`. If the version is too old, you may need to
[compile Vim from source][vim-build] (don't worry, it's easy).

Install iCompleteMe with [Vundle][].

**Remember:** iCM is a plugin with a compiled component. If you **update** iCM
using Vundle and the ycm_core library APIs have changed (happens
rarely), iCM will notify you to recompile it. You should then rerun the install
process.

Install development tools and CMake: 

    sudo apt-get install build-essential cmake

Make sure you have Python headers installed:

    sudo apt-get install python-dev python3-dev

    cd ~/.vim/bundle/iCompleteMe
    ./install.py


That's it. You're done. Refer to the _User Guide_ section on how to use iCM.
Don't forget that if you want the Swift semantic completion engine to work,
you will need to provide the compilation flags for your project to iCM. It's all
in the User Guide.

iCM comes with sane defaults for its options, but you still may want to take a
look at what's available for configuration. There are a few interesting options
that are conservatively turned off by default that you may want to turn on.

### Fedora Linux x64

Untested: Requires building [SwiftySwiftVim][] from source.

These instructions (using `install.py`) are the quickest way to install
iCompleteMe, however they may not work for everyone. If the following
instructions don't work for you, check out the [full installation
guide](#full-installation-guide).

Make sure you have Vim 7.4.1578 with Python 2 or Python 3 support. Fedora 21 and
later have a Vim that's recent enough. You can see the version of Vim installed
by running `vim --version`. If the version is too old, you may need to [compile
Vim from source][vim-build] (don't worry, it's easy).

Install iCompleteMe with [Vundle][].

**Remember:** iCM is a plugin with a compiled component. If you **update** iCM
using Vundle and the ycm_core library APIs have changed (happens
rarely), iCM will notify you to recompile it. You should then rerun the install
process.

Install development tools and CMake:

    sudo dnf install automake gcc gcc-c++ kernel-devel cmake

Make sure you have Python headers installed:

    sudo dnf install python-devel python3-devel

    cd ~/.vim/bundle/iCompleteMe
    ./install.py


That's it. You're done. Refer to the _User Guide_ section on how to use iCM.
Don't forget that if you want the Swift semantic completion engine to work,
you will need to provide the compilation flags for your project to iCM. It's all
in the User Guide.

iCM comes with sane defaults for its options, but you still may want to take a
look at what's available for configuration. There are a few interesting options
that are conservatively turned off by default that you may want to turn on.

### Windows

Untested: Requires building [SwiftySwiftVim][] from source.

These instructions (using `install.py`) are the quickest way to install
iCompleteMe, however they may not work for everyone. If the following
instructions don't work for you, check out the [full installation
guide](#full-installation-guide).

**Important:** we assume that you are using the `cmd.exe` command prompt and
that you know how to add an executable to the PATH environment variable.

Make sure you have at least Vim 7.4.1578 with Python 2 or Python 3 support. You
can check the version and which Python is supported by typing `:version` inside
Vim. Look at the features included: `+python/dyn` for Python 2 and
`+python3/dyn` for Python 3. Take note of the Vim architecture, i.e. 32 or
64-bit. It will be important when choosing the Python installer. We recommend
using a 64-bit client. [Daily updated copies of 32-bit and 64-bit Vim with
Python 2 and Python 3 support][vim-win-download] are available.

Install iCompleteMe with [Vundle][].

**Remember:** iCM is a plugin with a compiled component. If you **update** iCM
using Vundle and the ycm_core library APIs have changed (happens
rarely), iCM will notify you to recompile it. You should then rerun the install
process.

Download and install the following software:

- [Python 2 or Python 3][python-win-download]. Be sure to pick the version
corresponding to your Vim architecture. It is _Windows x86_ for a 32-bit Vim and
_Windows x86-64_ for a 64-bit Vim. We recommend installing Python 3.
- [CMake][cmake-download]. Add CMake executable to the PATH environment
variable.
- [Visual Studio][visual-studio-download]. Download the community edition.
During setup, select _Desktop development with C++_ in _Workloads_.

Compiling iCM **with** semantic support for Swift language:

    cd %USERPROFILE%/vimfiles/bundle/iCompleteMe
    install.py

You can specify the Microsoft Visual C++ (MSVC) version using the `--msvc`
option. iCM officially supports MSVC 12 (Visual Studio 2013), 14 (2015), and 15
(2017).

That's it. You're done. Refer to the _User Guide_ section on how to use iCM.

iCM comes with sane defaults for its options, but you still may want to take a
look at what's available for configuration. There are a few interesting options
that are conservatively turned off by default that you may want to turn on.

### FreeBSD/OpenBSD

Untested: Requires building [SwiftySwiftVim][] from source.

These instructions (using `install.py`) are the quickest way to install
iCompleteMe, however they may not work for everyone. If the following
instructions don't work for you, check out the [full installation
guide](#full-installation-guide).

**NOTE:** OpenBSD / FreeBSD are not officially supported platforms by iCM.

Make sure you have Vim 7.4.1578 with Python 2 or Python 3 support.

OpenBSD 5.5 and later have a Vim that's recent enough. You can see the version of
Vim installed by running `vim --version`.

FreeBSD 10.x comes with clang compiler but not the libraries needed to install.

    pkg install llvm38 boost-all boost-python-libs clang38
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/llvm38/lib/

Install iCompleteMe with [Vundle][].

**Remember:** iCM is a plugin with a compiled component. If you **update** iCM
using Vundle and the ycm_core library APIs have changed (happens
rarely), iCM will notify you to recompile it. You should then rerun the install
process.

Install dependencies and CMake: `sudo pkg_add llvm boost cmake`

    cd ~/.vim/bundle/iCompleteMe
    ./install.py 

That's it. You're done. Refer to the _User Guide_ section on how to use iCM.

iCM comes with sane defaults for its options, but you still may want to take a
look at what's available for configuration. There are a few interesting options
that are conservatively turned off by default that you may want to turn on.

### Full Installation Guide

These are the steps necessary to get iCM working on a Unix OS and on Windows.

**Note to Windows users:** we assume that you are running the `cmd.exe` command
prompt and that the needed executables are in the PATH environment variable. Do
not just copy the shell commands. Replace `~` by `%USERPROFILE%` in them and use
the right Vim home directory. It should be `vimfiles` by default instead of
`.vim`.

See the _FAQ_ if you have any issues.

**Remember:** iCM is a plugin with a compiled component. If you **update** iCM
using Vundle and the ycm_core library APIs have changed (happens
rarely), iCM will notify you to recompile it. You should then rerun the install
process.

**Please follow the instructions carefully. Read EVERY WORD.**

1.  **Ensure that your version of Vim is _at least_ 7.4.1578 _and_ that it has
    support for Python 2 or Python 3 scripting**.

    Inside Vim, type `:version`. Look at the first two to three lines of output;
    it should say `Vi IMproved X.Y`, where X.Y is the major version of vim. If
    your version is greater than 7.4, then you're all set. If your version is
    7.4 then look below that where it says, `Included patches: 1-Z`, where Z
    will be some number. That number needs to be 143 or higher.

    If your version of Vim is not recent enough, you may need to [compile Vim
    from source][vim-build] (don't worry, it's easy).

    After you have made sure that you have Vim 7.4.1578+, type the following in
    Vim: `:echo has('python') || has('python3')`. The output should be 1. If
    it's 0, then get a version of Vim with Python support.

    On Windows, check also if your Vim architecture is 32 or 64-bit. This is
    critical because it must match the Python and the iCM libraries
    architectures. We recommend using a 64-bit Vim.

2.  **Install iCM** with [Vundle][] (or [Pathogen][], but Vundle is a better
    idea). With Vundle, this would mean adding a `Plugin
    'jerrymarino/iCompleteMe'` line to your [vimrc][].

    If you don't install iCM with Vundle, make sure you have run
    `git submodule update --init --recursive` after checking out the iCM
    repository (Vundle will do this for you) to fetch iCM's dependencies.

4.  **Compile the `ycm_core` library** that iCM needs. This library
    is the C++ engine that iCM uses to get fast completions.

    You will need to have `cmake` installed in order to generate the required
    makefiles. Linux users can install cmake with their package manager (`sudo
    apt-get install cmake` for Ubuntu) whereas other users can [download and
    install][cmake-download] cmake from its project site. Mac users can also get
    it through [Homebrew][brew] with `brew install cmake`.

    On a Unix OS, you need to make sure you have Python headers installed. On a
    Debian-like Linux distro, this would be `sudo apt-get install python-dev
    python3-dev`. On Mac they should already be present.

    On Windows, you need to download and install [Python 2 or
    Python 3][python-win-download]. Pick the version corresponding to your Vim
    architecture. You will also need Microsoft Visual C++ (MSVC) to build iCM.
    You can obtain it by installing [Visual Studio][visual-studio-download].
    MSVC 12 (Visual Studio 2013), 14 (2015), and 15 (2017) are officially
    supported.

    Here we'll assume you installed iCM with Vundle. That means that the
    top-level iCM directory is in `~/.vim/bundle/iCompleteMe`.

    We'll create a new folder where build files will be placed. Run the
    following:

        cd ~
        mkdir ycm_build
        cd ycm_build

    Now we need to generate the makefiles. If you DON'T care about semantic
    support for Swift language, run the following command in the `ycm_build`
    directory:

        cmake -G "<generator>" . ~/.vim/bundle/iCompleteMe/third_party/ycmd/cpp

    where `<generator>` is `Unix Makefiles` on Unix systems and one of the
    following Visual Studio generators on Windows:

    - `Visual Studio 12 Win64`
    - `Visual Studio 14 Win64`
    - `Visual Studio 15 Win64`

    Remove the `Win64` part in these generators if your Vim architecture is
    32-bit.

    For those who want to use the system version of boost, you would pass
    `-DUSE_SYSTEM_BOOST=ON` to cmake. This may be necessary on some systems
    where the bundled version of boost doesn't compile out of the box.

    **NOTE:** We **STRONGLY recommend AGAINST use** of the system boost instead
    of the bundled version of boost. Random things may break. Save yourself
    the hassle and use the bundled version of boost.


    With that in mind, run the following command in the `ycm_build` directory:

        cmake -G "<generator>" -DPATH_TO_LLVM_ROOT=~/ycm_temp/llvm_root_dir . ~/.vim/bundle/iCompleteMe/third_party/ycmd/cpp

    where `<generator>` is replaced like above.

    Now that configuration files have been generated, compile the libraries
    using this command:

        cmake --build . --target ycm_core --config Release

    The `--config Release` part is specific to Windows and will be ignored on a
    Unix OS.

    For those who want to use the system version of libclang, you would pass
    `-DUSE_SYSTEM_LIBCLANG=ON` to cmake _instead of_ the
    `-DPATH_TO_LLVM_ROOT=...` flag.

    **NOTE:** We **STRONGLY recommend AGAINST use** of the system libclang instead
    of the upstream compiled binaries. Random things may break. Save yourself
    the hassle and use the upstream pre-built libclang.

    You could also force the use of a custom libclang library with
    `-DEXTERNAL_LIBCLANG_PATH=/path/to/libclang.so` flag (the library would end
    with `.dylib` on a Mac). Again, this flag would be used _instead of_ the
    other flags. **If you compiled LLVM from source, this is the flag you should
    be using.**

    Running the `cmake` command will also place the `libclang.[so|dylib|dll]` in
    the `iCompleteMe/third_party/ycmd` folder for you if you compiled with
    clang support (it needs to be there for iCM to work).

That's it. You're done. Refer to the _User Guide_ section on how to use iCM.

iCM comes with sane defaults for its options, but you still may want to take a
look at what's available for configuration. There are a few interesting options
that are conservatively turned off by default that you may want to turn on.

Quick Feature Summary
-----

* Super-fast identifier completer including tags files and syntax elements
* Intelligent suggestion ranking and filtering
* File and path suggestions
* Suggestions from Vim's OmniFunc
* UltiSnips snippet suggestions

User Guide
----------

### General Usage

- If the offered completions are too broad, keep typing characters; iCM will
  continue refining the offered completions based on your input.
- Filtering is "smart-case" sensitive; if you are typing only lowercase letters,
  then it's case-insensitive. If your input contains uppercase letters, then the
  uppercase letters in your query must match uppercase letters in the completion
  strings (the lowercase letters still match both). So, "foo" matches "Foo" and
  "foo", "Foo" matches "Foo" and "FOO" but not "foo".
- Use the TAB key to accept a completion and continue pressing TAB to cycle
  through the completions. Use Shift-TAB to cycle backwards. Note that if you're
  using console Vim (that is, not Gvim or MacVim) then it's likely that the
  Shift-TAB binding will not work because the console will not pass it to Vim.
  You can remap the keys; see the _[Options][]_ section below.

Knowing a little bit about how iCM works internally will prevent confusion. iCM
has several completion engines: an identifier-based completer that collects all
of the identifiers in the current file and other files you visit (and your tags
files) and searches them when you type (identifiers are put into per-filetype
groups).


### Client-Server Architecture

iCM has a client-server architecture; the Vim part of iCM is only a thin client
that talks to the [ycmd HTTP+JSON server][ycmd] that has the vast majority of
iCM logic and functionality. The server is started and stopped automatically as
you start and stop Vim.

### Completion String Ranking

The subsequence filter removes any completions that do not match the input, but
then the sorting system kicks in. It's actually very complicated and uses lots
of factors, but suffice it to say that "word boundary" (WB) subsequence
character matches are "worth" more than non-WB matches. In effect, this means
given an input of "gua", the completion "getUserAccount" would be ranked higher
in the list than the "Fooguxa" completion (both of which are subsequence
matches). A word-boundary character are all capital characters, characters
preceded by an underscore and the first letter character in the completion
string.

### General Semantic Completion

- You can use Ctrl+Space to trigger the completion suggestions anywhere, even
  without a string prefix. This is useful to see which top-level functions are
  available for use.

### Semantic Compliation

#### Setup a [compilation database][compdb]

By default, it provides a basic level of completion support: completions within
a single file.

In most cases, build options and dependencies need to be specified to have a
good experience.

SwiftySwiftVim uses a [Compilation
Database](http://clang.llvm.org/docs/JSONCompilationDatabase.html) to import
compiler settings. Setup the build system to generate one at the workspace
root.

For Xcode *Project* users, [XcodeCompilationDatabase
](https://github.com/jerrymarino/XcodeCompilationDatabase) makes this easy.


### Diagnostic Display

iCM will display diagnostic notifications for if you. Diagnostics will
also be displayed for TypeScript. Since iCM continuously recompiles your file as
you type, you'll get notified of errors and warnings in your file as fast as
possible.

Here are the various pieces of the diagnostic UI:

- Icons show up in the Vim gutter on lines that have a diagnostic.
- Regions of text related to diagnostics are highlighted (by default, a red
  wavy underline in `gvim` and a red background in `vim`).
- Moving the cursor to a line with a diagnostic echoes the diagnostic text.
- Vim's location list is automatically populated with diagnostic data (off by
  default, see options).

The new diagnostics (if any) will be displayed the next time you press any key
on the keyboard. So if you stop typing and just wait for the new diagnostics to
come in, that _will not work_. You need to press some key for the GUI to update.

Having to press a key to get the updates is unfortunate, but cannot be changed
due to the way Vim internals operate; there is no way that a background task can
update Vim's GUI after it has finished running.  You _have to_ press a key. This
will make iCM check for any pending diagnostics updates.

You _can_ force a full, blocking compilation cycle with the
`:IcmForceCompileAndDiagnostics` command (you may want to map that command to a
key; try putting `nnoremap <F5> :IcmForceCompileAndDiagnostics<CR>` in your
vimrc). Calling this command will force iCM to immediately recompile your file
and display any new diagnostics it encounters. Do note that recompilation with
this command may take a while and during this time the Vim GUI _will_ be
blocked.

iCM will display a short diagnostic message when you move your cursor to the
line with the error. You can get a detailed diagnostic message with the
`<leader>d` key mapping (can be changed in the options) iCM provides when your
cursor is on the line with the diagnostic.

You can also see the full diagnostic message for all the diagnostics in the
current file in Vim's `locationlist`, which can be opened with the `:lopen` and
`:lclose` commands (make sure you have set `let
g:icm_always_populate_location_list = 1` in your vimrc). A good way to toggle
the display of the `locationlist` with a single key mapping is provided by
another (very small) Vim plugin called [ListToggle][] (which also makes it
possible to change the height of the `locationlist` window), also written by
yours truly.

#### Diagnostic Highlighting Groups

You can change the styling for the highlighting groups iCM uses. For the signs
in the Vim gutter, the relevant groups are:

- `IcmErrorSign`, which falls back to group `SyntasticErrorSign` and then
  `error` if they exist
- `IcmWarningSign`, which falls back to group `SyntasticWarningSign` and then
  `todo` if they exist

You can also style the line that has the warning/error with these groups:

- `IcmErrorLine`, which falls back to group `SyntasticErrorLine` if it exists
- `IcmWarningLine`, which falls back to group `SyntasticWarningLine` if it
  exists

Note that the line highlighting groups only work when gutter signs are turned
on.

The syntax groups used to highlight regions of text with errors/warnings:
- `IcmErrorSection`, which falls back to group `SyntasticError` if it exists and
  then `SpellBad`
- `IcmWarningSection`, which falls back to group `SyntasticWarning` if it exists
  and then `SpellCap`

Here's how you'd change the style for a group:

```viml
highlight IcmErrorLine guibg=#3f0000
```

Commands
--------

### The `:IcmRestartServer` command

If the [ycmd completion server][ycmd] suddenly stops for some reason, you can
restart it with this command.

### The `:IcmForceCompileAndDiagnostics` command

Calling this command will force iCM to immediately recompile your file
and display any new diagnostics it encounters. Do note that recompilation with
this command may take a while and during this time the Vim GUI _will_ be
blocked.

You may want to map this command to a key; try putting `nnoremap <F5>
:IcmForceCompileAndDiagnostics<CR>` in your vimrc.

### The `:IcmDiags` command

Calling this command will fill Vim's `locationlist` with errors or warnings if
any were detected in your file and then open it. If a given error or warning can
be fixed by a call to `:IcmCompleter FixIt`, then ` (FixIt available)` is
appended to the error or warning text. See the `FixIt` completer subcommand for
more information.

**NOTE:** The absense of ` (FixIt available)` does not strictly imply a fix-it
is not available as not all completers are able to provide this indication. For
example, the swift completer provides many fix-its but does not add this
additional indication.

The `g:icm_open_loclist_on_ycm_diags` option can be used to prevent the location
list from opening, but still have it filled with new diagnostic data. See the
_Options_ section for details.

### The `:IcmShowDetailedDiagnostic` command

This command shows the full diagnostic text when the user's cursor is on the
line with the diagnostic.

### The `:IcmDebugInfo` command

This will print out various debug information for the current file. Useful to
see what compile commands will be used for the file if you're using the semantic
completion engine.

### The `:IcmToggleLogs` command

This command opens in separate windows the logfiles given as arguments or closes
them if they are already open in the editor. When no argument is given, list the
available logfiles. Only for debugging purpose.

### The `:IcmCompleter` command

This command gives access to a number of additional [IDE-like
features](#quick-feature-summary).

Technically the command invokes completer-specific commands.  If the first
argument is of the form `ft=...` the completer for that file type will be used
(for example `ft=cpp`), else the native completer of the current buffer will be
used.
Call `IcmCompleter` without further arguments for a list of the
commands you can call for the current completer.

See the [file type feature summary](#quick-feature-summary) for an overview of
the features available for each file type. See the _IcmCompleter subcommands_
section for more information on the available subcommands and their usage.

### Miscellaneous Commands

These commands are for general administration, rather than IDE-like features.
They cover things like the semantic engine server instance and compilation
flags.

#### The `RestartServer` subcommand

Restarts the semantic-engine-as-localhost-server for those semantic engines that
work as separate servers that iCM talks to.

An additional optional argument may be supplied for Python, specifying the
python binary to use to restart the Python semantic engine.

```viml
:IcmCompleter RestartServer /usr/bin/python3.4
```

#### The `ClearCompilationFlagCache` subcommand

TODO:Jerry ( Not Implemented )

iCM caches the flags it gets from the `FlagsForFile` function in your
`ycm_extra_conf.py` file if you return them with the `do_cache` parameter set to
`True`. The cache is in memory and is never invalidated (unless you restart Vim
of course).

This command clears that cache entirely. iCM will then re-query your
`FlagsForFile` function as needed in the future.

Functions
--------

### The `icompleteme#GetErrorCount` function

Get the number of iCM Diagnostic errors. If no errors are present, this function
returns 0.

For example:
```viml
  call icompleteme#GetErrorCount()
```

Both this function and `icompleteme#GetWarningCount` can be useful when
integrating iCM with other Vim plugins. For example, a [lightline][] user could
add a diagnostics section to their statusline which would display the number of
errors and warnings.

### The `icompleteme#GetWarningCount` function

Get the number of iCM Diagnostic warnings. If no warnings are present, this
function returns 0.

For example:
```viml
  call icompleteme#GetWarningCount()
```

Autocommands
------------

### The `IcmLocationOpened` autocommand

This `User` autocommand is fired when iCM opens the location list window in
response to the `IcmDiags` command. By default, the location list window is
opened to full width at the bottom of the screen and its height is set to fit
all entries. This behavior can be overridden by using the `IcmLocationOpened`
autocommand which is triggered while the cursor is in the location list window.
For instance:
```viml
function! s:CustomizeIcmLocationWindow()
  " Move the window to the top of the screen.
  wincmd K
  " Set the window height to 5.
  5wincmd _
  " Switch back to working window.
  wincmd p
endfunction

autocmd User IcmLocationOpened call s:CustomizeIcmLocationWindow()
```

### The `IcmQuickFixOpened` autocommand

This `User` autocommand is fired when iCM opens the quickfix window in response
to the `GoTo*` and `RefactorRename` subcommands. By default, the quickfix window
is opened to full width at the bottom of the screen and its height is set to fit
all entries. This behavior can be overridden by using the `IcmQuickFixOpened`
autocommand which is triggered while the cursor is in the quickfix window. For
instance:
```viml
function! s:CustomizeIcmQuickFixWindow()
  " Move the window to the top of the screen.
  wincmd K
  " Set the window height to 5.
  5wincmd _
endfunction

autocmd User IcmQuickFixOpened call s:CustomizeIcmQuickFixWindow()
```

Options
-------

All options have reasonable defaults so if the plug-in works after installation
you don't need to change any options. These options can be configured in your
[vimrc script][vimrc] by including a line like this:

```viml
let g:icm_min_num_of_chars_for_completion = 1
```

Note that after changing an option in your [vimrc script][vimrc] you have to
restart Vim for the changes to take effect.

### The `g:icm_min_num_of_chars_for_completion` option

This option controls the number of characters the user needs to type before
identifier-based completion suggestions are triggered. For example, if the
option is set to `2`, then when the user types a second alphanumeric character
after a whitespace character, completion suggestions will be triggered. This
option is NOT used for semantic completion.

Setting this option to a high number like `99` effectively turns off the
identifier completion engine and just leaves the semantic engine.

Default: `2`

```viml
let g:icm_min_num_of_chars_for_completion = 2
```

### The `g:icm_min_num_identifier_candidate_chars` option

This option controls the minimum number of characters that a completion
candidate coming from the identifier completer must have to be shown in the
popup menu.

A special value of `0` means there is no limit.

**NOTE:** This option only applies to the identifier completer; it has no effect
on the various semantic completers.

Default: `0`

```viml
let g:icm_min_num_identifier_candidate_chars = 0
```

### The `g:icm_auto_trigger` option

When set to `0`, this option turns off iCM's identifier completer (the
as-you-type popup) _and_ the semantic triggers (the popup you'd get after typing
`.` or `->` in say C++). You can still force semantic completion with the
`<C-Space>` shortcut.

If you want to just turn off the identifier completer but keep the semantic
triggers, you should set `g:icm_min_num_of_chars_for_completion` to a high
number like `99`.

Default: `1`

```viml
let g:icm_auto_trigger = 1
```

### The `g:icm_filetype_whitelist` option

This option controls for which Vim filetypes (see `:h filetype`) should iCM be
turned on. The option value should be a Vim dictionary with keys being filetype
strings (like `python`, `cpp` etc) and values being unimportant (the dictionary
is used like a hash set, meaning that only the keys matter).

The `*` key is special and matches all filetypes. By default, the whitelist
contains only this `*` key.

iCM also has a `g:icm_filetype_blacklist` option that lists filetypes for which
iCM shouldn't be turned on. iCM will work only in filetypes that both the
whitelist and the blacklist allow (the blacklist "allows" a filetype by _not_
having it as a key).

For example, let's assume you want iCM to work in files with the `cpp` filetype.
The filetype should then be present in the whitelist either directly (`cpp` key
in the whitelist) or indirectly through the special `*` key. It should _not_ be
present in the blacklist.

Filetypes that are blocked by the either of the lists will be completely ignored
by iCM, meaning that neither the identifier-based completion engine nor the
semantic engine will operate in them.

You can get the filetype of the current file in Vim with `:set ft?`.

Default: `{'swift' : 1}`

```viml
let g:icm_filetype_whitelist = { 'swift': 1 }
```

### The `g:icm_filetype_blacklist` option

This option controls for which Vim filetypes (see `:h filetype`) should iCM be
turned off. The option value should be a Vim dictionary with keys being filetype
strings (like `python`, `cpp` etc) and values being unimportant (the dictionary
is used like a hash set, meaning that only the keys matter).

See the `g:icm_filetype_whitelist` option for more details on how this works.

Default: `[see next line]`

```viml
let g:icm_filetype_blacklist = {
      \ 'tagbar' : 1,
      \ 'qf' : 1,
      \ 'notes' : 1,
      \ 'markdown' : 1,
      \ 'unite' : 1,
      \ 'text' : 1,
      \ 'vimwiki' : 1,
      \ 'pandoc' : 1,
      \ 'infolog' : 1,
      \ 'mail' : 1
      \}
```

### The `g:icm_filetype_specific_completion_to_disable` option

This option controls for which Vim filetypes (see `:h filetype`) should the iCM
semantic completion engine be turned off. The option value should be a Vim
dictionary with keys being filetype strings (like `python`, `cpp` etc) and
values being unimportant (the dictionary is used like a hash set, meaning that
only the keys matter). The listed filetypes will be ignored by the iCM semantic
completion engine, but the identifier-based completion engine will still trigger
in files of those filetypes.

Note that even if semantic completion is not turned off for a specific filetype,
you will not get semantic completion if the semantic engine does not support
that filetype.

You can get the filetype of the current file in Vim with `:set ft?`.

Default: `[see next line]`

```viml
let g:icm_filetype_specific_completion_to_disable = {
      \ 'gitcommit': 1
      \}
```

### The `g:icm_show_diagnostics_ui` option

When set, this option turns on iCM's diagnostic display features. See the
_Diagnostic display_ section in the _User Manual_ for more details.

Specific parts of the diagnostics UI (like the gutter signs, text highlighting,
diagnostic echo and auto location list population) can be individually turned on
or off. See the other options below for details.

When set, this option also makes iCM remove all Syntastic checkers set for the
`swift` filetype since this would conflict with iCM's own diagnostics UI.

Unset to use with Syntastic diagnostic checkers.

Default: `1`

```viml
let g:icm_show_diagnostics_ui = 1
```

### The `g:icm_error_symbol` option

iCM will use the value of this option as the symbol for errors in the Vim
gutter.

This option is part of the Syntastic compatibility layer; if the option is not
set, iCM will fall back to the value of the `g:syntastic_error_symbol` option
before using this option's default.

Default: `>>`

```viml
let g:icm_error_symbol = '>>'
```

### The `g:icm_warning_symbol` option

iCM will use the value of this option as the symbol for warnings in the Vim
gutter.

This option is part of the Syntastic compatibility layer; if the option is not
set, iCM will fall back to the value of the `g:syntastic_warning_symbol` option
before using this option's default.

Default: `>>`

```viml
let g:icm_warning_symbol = '>>'
```

### The `g:icm_enable_diagnostic_signs` option

When this option is set, iCM will put icons in Vim's gutter on lines that have a
diagnostic set. Turning this off will also turn off the `IcmErrorLine` and
`IcmWarningLine` highlighting.

This option is part of the Syntastic compatibility layer; if the option is not
set, iCM will fall back to the value of the `g:syntastic_enable_signs` option
before using this option's default.

Default: `1`

```viml
let g:icm_enable_diagnostic_signs = 1
```

### The `g:icm_enable_diagnostic_highlighting` option

When this option is set, iCM will highlight regions of text that are related to
the diagnostic that is present on a line, if any.

This option is part of the Syntastic compatibility layer; if the option is not
set, iCM will fall back to the value of the `g:syntastic_enable_highlighting`
option before using this option's default.

Default: `1`

```viml
let g:icm_enable_diagnostic_highlighting = 1
```

### The `g:icm_echo_current_diagnostic` option

When this option is set, iCM will echo the text of the diagnostic present on the
current line when you move your cursor to that line. If a `FixIt` is available
for the current diagnostic, then ` (FixIt)` is appended.

This option is part of the Syntastic compatibility layer; if the option is not
set, iCM will fall back to the value of the `g:syntastic_echo_current_error`
option before using this option's default.

Default: `1`

```viml
let g:icm_echo_current_diagnostic = 1
```

### The `g:icm_filter_diagnostics` option

This option controls which diagnostics will be rendered by iCM. This option
holds a dictionary of key-values, where the keys are Vim's filetype strings
delimited by commas and values are dictionaries describing the filter.

A filter is a dictionary of key-values, where the keys are the type of filter,
and the value is a list of arguments to that filter. In the case of just a
single item in the list, you may omit the brackets and just provide the argument
directly. If any filter matches a diagnostic, it will be dropped and iCM will 
not render it.

The following filter types are supported:

- "regex": Accepts a string [regular expression][python-re]. This type matches
when the regex (treated as case-insensitive) is found in the diagnostic text.
- "level": Accepts a string level, either "warning" or "error." This type 
matches when the diagnostic has the same level.

**NOTE:** The regex syntax is **NOT** Vim's, it's [Python's][python-re].

Default: `{}`

```viml
let g:icm_filter_diagnostics = {
  \ "java": {
  \      "regex": [ ".*taco.*", ... ],
  \      "level": "error",
  \      ...
  \    }
  \ }
```

### The `g:icm_always_populate_location_list` option

When this option is set, iCM will populate the location list automatically every
time it gets new diagnostic data. This option is off by default so as not to
interfere with other data you might have placed in the location list.

See `:help location-list` in Vim to learn more about the location list.

This option is part of the Syntastic compatibility layer; if the option is not
set, iCM will fall back to the value of the
`g:syntastic_always_populate_loc_list` option before using this option's
default.

Default: `0`

```viml
let g:icm_always_populate_location_list = 0
```

### The `g:icm_open_loclist_on_ycm_diags` option

When this option is set, `:IcmDiags` will automatically open the location list
after forcing a compilation and filling the list with diagnostic data.

See `:help location-list` in Vim to learn more about the location list.

Default: `1`

```viml
let g:icm_open_loclist_on_ycm_diags = 1
```

### The `g:icm_complete_in_comments` option

When this option is set to `1`, iCM will show the completion menu even when
typing inside comments.

Default: `0`

```viml
let g:icm_complete_in_comments = 0
```

### The `g:icm_complete_in_strings` option

When this option is set to `1`, iCM will show the completion menu even when
typing inside strings.

Default: `1`

```viml
let g:icm_complete_in_strings = 1
```

### The `g:icm_collect_identifiers_from_comments_and_strings` option

When this option is set to `1`, iCM's identifier completer will also collect
identifiers from strings and comments. Otherwise, the text in comments and
strings will be ignored.

Default: `0`

```viml
let g:icm_collect_identifiers_from_comments_and_strings = 0
```

### The `g:icm_collect_identifiers_from_tags_files` option

When this option is set to `1`, iCM's identifier completer will also collect
identifiers from tags files. The list of tags files to examine is retrieved from
the `tagfiles()` Vim function which examines the `tags` Vim option. See `:h
'tags'` for details.

iCM will re-index your tags files if it detects that they have been modified.

The only supported tag format is the [Exuberant Ctags format][ctags-format]. The
format from "plain" ctags is NOT supported. Ctags needs to be called with the
`--fields=+l` option (that's a lowercase `L`, not a one) because iCM needs the
`language:<lang>` field in the tags output.

See the _FAQ_ for pointers if iCM does not appear to read your tag files.

This option is off by default because it makes Vim slower if your tags are on a
network directory.

Default: `0`

```viml
let g:icm_collect_identifiers_from_tags_files = 0
```

### The `g:icm_seed_identifiers_with_syntax` option

When this option is set to `1`, iCM's identifier completer will seed its
identifier database with the keywords of the programming language you're
writing.

Since the keywords are extracted from the Vim syntax file for the filetype, all
keywords may not be collected, depending on how the syntax file was written.
Usually at least 95% of the keywords are successfully extracted.

Default: `0`

```viml
let g:icm_seed_identifiers_with_syntax = 0
```

### The `g:icm_server_python_interpreter` option

iCM will by default search for an appropriate Python interpreter on your system.
You can use this option to override that behavior and force the use of a
specific interpreter of your choosing.

**NOTE:** This interpreter is only used for the [ycmd server][ycmd]. The iCM
client running inside Vim always uses the Python interpreter that's embedded
inside Vim.

Default: `''`

```viml
let g:icm_server_python_interpreter = ''
```

### The `g:icm_keep_logfiles` option

When this option is set to `1`, iCM and the [ycmd completion server][ycmd] will
keep the logfiles around after shutting down (they are deleted on shutdown by
default).

To see where the logfiles are, call `:IcmDebugInfo`.

Default: `0`

```viml
let g:icm_keep_logfiles = 0
```

### The `g:icm_log_level` option

The logging level that iCM and the [ycmd completion server][ycmd] use. Valid
values are the following, from most verbose to least verbose:
- `debug`
- `info`
- `warning`
- `error`
- `critical`

Note that `debug` is _very_ verbose.

Default: `info`

```viml
let g:icm_log_level = 'info'
```

### The `g:icm_add_preview_to_completeopt` option

When this option is set to `1`, iCM will add the `preview` string to Vim's
`completeopt` option (see `:h completeopt`). If your `completeopt` option
already has `preview` set, there will be no effect. You can see the current
state of your `completeopt` setting with `:set completeopt?` (yes, the question
mark is important).

When `preview` is present in `completeopt`, iCM will use the `preview` window at
the top of the file to store detailed information about the current completion
candidate (but only if the candidate came from the semantic engine). For
instance, it would show the full function prototype and all the function
overloads in the window if the current completion is a function name.

Default: `0`

```viml
let g:icm_add_preview_to_completeopt = 0
```

### The `g:icm_autoclose_preview_window_after_completion` option

When this option is set to `1`, iCM will auto-close the `preview` window after
the user accepts the offered completion string. If there is no `preview` window
triggered because there is no `preview` string in `completeopt`, this option is
irrelevant. See the `g:icm_add_preview_to_completeopt` option for more details.

Default: `0`

```viml
let g:icm_autoclose_preview_window_after_completion = 0
```

### The `g:icm_autoclose_preview_window_after_insertion` option

When this option is set to `1`, iCM will auto-close the `preview` window after
the user leaves insert mode. This option is irrelevant if
`g:icm_autoclose_preview_window_after_completion` is set or if no `preview`
window is triggered. See the `g:icm_add_preview_to_completeopt` option for more
details.

Default: `0`

```viml
let g:icm_autoclose_preview_window_after_insertion = 0
```

### The `g:icm_max_diagnostics_to_display` option

This option controls the maximum number of diagnostics shown to the user when
errors or warnings are detected in the file.

Default: `30`

```viml
let g:icm_max_diagnostics_to_display = 30
```

### The `g:icm_key_list_select_completion` option

This option controls the key mappings used to select the first completion
string.  Invoking any of them repeatedly cycles forward through the completion
list.

Some users like adding `<Enter>` to this list.

Default: `['<TAB>', '<Down>']`

```viml
let g:icm_key_list_select_completion = ['<TAB>', '<Down>']
```

### The `g:icm_key_list_previous_completion` option

This option controls the key mappings used to select the previous completion
string. Invoking any of them repeatedly cycles backwards through the completion
list.

Note that one of the defaults is `<S-TAB>` which means Shift-TAB. That mapping
will probably only work in GUI Vim (Gvim or MacVim) and not in plain console Vim
because the terminal usually does not forward modifier key combinations to Vim.

Default: `['<S-TAB>', '<Up>']`

```viml
let g:icm_key_list_previous_completion = ['<S-TAB>', '<Up>']
```

### The `g:icm_key_invoke_completion` option

This option controls the key mapping used to invoke the completion menu for
semantic completion. By default, semantic completion is trigged automatically
after typing `.`, `->` and `::` in insert mode (if semantic completion support
has been compiled in). This key mapping can be used to trigger semantic
completion anywhere. Useful for searching for top-level functions and classes.

Console Vim (not Gvim or MacVim) passes `<Nul>` to Vim when the user types
`<C-Space>` so iCM will make sure that `<Nul>` is used in the map command when
you're editing in console Vim, and `<C-Space>` in GUI Vim. This means that you
can just press `<C-Space>` in both console and GUI Vim and iCM will do the right
thing.

Setting this option to an empty string will make sure no mapping is created.

Default: `<C-Space>`

```viml
let g:icm_key_invoke_completion = '<C-Space>'
```

### The `g:icm_key_detailed_diagnostics` option

This option controls the key mapping used to show the full diagnostic text when
the user's cursor is on the line with the diagnostic. It basically calls
`:IcmShowDetailedDiagnostic`.

Setting this option to an empty string will make sure no mapping is created.

Default: `<leader>d`

```viml
let g:icm_key_detailed_diagnostics = '<leader>d'
```

### The `g:icm_global_ycm_extra_conf` option

Normally, iCM searches for a `.ycm_extra_conf.py` file for compilation flags
(see the User Guide for more details on how this works). This option specifies
a fallback path to a config file which is used if no `.ycm_extra_conf.py` is
found.

You can place such a global file anywhere in your filesystem.

Default: `''`

```viml
let g:icm_global_ycm_extra_conf = ''
```

### The `g:icm_confirm_extra_conf` option

When this option is set to `1` iCM will ask once per `.ycm_extra_conf.py` file
if it is safe to be loaded. This is to prevent execution of malicious code
from a `.ycm_extra_conf.py` file you didn't write.

To selectively get iCM to ask/not ask about loading certain `.ycm_extra_conf.py`
files, see the `g:icm_extra_conf_globlist` option.

Default: `1`

```viml
let g:icm_confirm_extra_conf = 1
```

### The `g:icm_extra_conf_globlist` option

This option is a list that may contain several globbing patterns. If a pattern
starts with a `!` all `.ycm_extra_conf.py` files matching that pattern will be
blacklisted, that is they won't be loaded and no confirmation dialog will be
shown. If a pattern does not start with a `!` all files matching that pattern
will be whitelisted. Note that this option is not used when confirmation is
disabled using `g:icm_confirm_extra_conf` and that items earlier in the list
will take precedence over the later ones.

Rules:

* `*`       matches everything
* `?`       matches any single character
* `[seq]`   matches any character in seq
* `[!seq]`  matches any char not in seq

Example:

```viml
let g:icm_extra_conf_globlist = ['~/dev/*','!~/*']
```

* The first rule will match everything contained in the `~/dev` directory so
  `.ycm_extra_conf.py` files from there will be loaded.
* The second rule will match everything in the home directory so a
  `.ycm_extra_conf.py` file from there won't be loaded.
* As the first rule takes precedence everything in the home directory excluding
  the `~/dev` directory will be blacklisted.

**NOTE:** The glob pattern is first expanded with Python's
`os.path.expanduser()` and then resolved with `os.path.abspath()` before being
matched against the filename.

Default: `[]`

```viml
let g:icm_extra_conf_globlist = []
```

### The `g:icm_filepath_completion_use_working_dir` option

By default, iCM's filepath completion will interpret relative paths like `../`
as being relative to the folder of the file of the currently active buffer.
Setting this option will force iCM to always interpret relative paths as being
relative to Vim's current working directory.

Default: `0`

```viml
let g:icm_filepath_completion_use_working_dir = 0
```

### The `g:icm_semantic_triggers` option

This option controls the character-based triggers for the various semantic
completion engines. The option holds a dictionary of key-values, where the keys
are Vim's filetype strings delimited by commas and values are lists of strings,
where the strings are the triggers.

Setting key-value pairs on the dictionary _adds_ semantic triggers to the
internal default set (listed below). You cannot remove the default triggers,
only add new ones.

A "trigger" is a sequence of one or more characters that trigger semantic
completion when typed. For instance, C++ (`cpp` filetype) has `.` listed as a
trigger. So when the user types `foo.`, the semantic engine will trigger and
serve `foo`'s list of member functions and variables. Since C++ also has `->`
listed as a trigger, the same thing would happen when the user typed `foo->`.

It's also possible to use a regular expression as a trigger. You have to prefix
your trigger with `re!` to signify it's a regex trigger. For instance,
`re!\w+\.` would only trigger after the `\w+\.` regex matches.

**NOTE:** The regex syntax is **NOT** Vim's, it's [Python's][python-re].

Default: `[see next line]`

```viml
let g:icm_semantic_triggers =  {
  \   'swift' : ['.', '[_a-zA-Z'],
  \ }
```

### The `g:icm_cache_omnifunc` option

Some omnicompletion engines do not work well with the iCM cache—in particular,
they might not produce all possible results for a given prefix. By unsetting
this option you can ensure that the omnicompletion engine is re-queried on every
keypress. That will ensure all completions will be presented, but might cause
stuttering and lagginess if the omnifunc is slow.

Default: `1`

```viml
let g:icm_cache_omnifunc = 1
```

### The `g:icm_use_ultisnips_completer` option

By default, iCM will query the UltiSnips plugin for possible completions of
snippet triggers. This option can turn that behavior off.

Default: `1`

```viml
let g:icm_use_ultisnips_completer = 1
```

### The `g:icm_goto_buffer_command` option

Defines where `GoTo*` commands result should be opened.
Can take one of the following values:
`[ 'same-buffer', 'horizontal-split', 'vertical-split', 'new-tab',
  'new-or-existing-tab' ]`
If this option is set to the `'same-buffer'` but current buffer can not
be switched (when buffer is modified and `nohidden` option is set),
then result will be opened in horizontal split.

Default: `'same-buffer'`

```viml
let g:icm_goto_buffer_command = 'same-buffer'
```

### The `g:icm_disable_for_files_larger_than_kb` option

Defines the max size (in Kb) for a file to be considered for completion. If this
option is set to 0 then no check is made on the size of the file you're opening.

Default: 1000

```viml
let g:icm_disable_for_files_larger_than_kb = 1000
```

### The `g:icm_python_binary_path` option

*TODO:jerry Remove ( I don't think we need this )*

This option specifies the Python interpreter to use to run the [jedi][]
completion library.  Specify the Python interpreter to use to get completions.
By default the Python under which [ycmd][] runs is used ([ycmd][] runs on
Python 2.6, 2.7 or 3.3+).

Default: `''`

```viml
let g:icm_python_binary_path = 'python'
```

**NOTE:** the settings above will make iCM use the first `python` executable
found through the PATH.

FAQ
---

### I used to be able to `import vim` in `.ycm_extra_conf.py`, but now can't

iCM was rewritten to use a client-server architecture where most of the logic is
in the [ycmd server][ycmd]. So the magic `vim` module you could have previously
imported in your `.ycm_extra_conf.py` files doesn't exist anymore.

To be fair, importing the magic `vim` module in extra conf files was never
supported in the first place; it only ever worked by accident and was never a
part of the extra conf API.

But fear not, you should be able to tweak your extra conf files to continue
working by using the `g:icm_extra_conf_vim_data` option. See the docs on that
option for details.

### I get `ImportError` exceptions that mention `PyInit_ycm_core` or `initycm_core`

These errors are caused by building the iCM native libraries for Python 2 and
trying to load them into a Python 3 process (or the other way around).

For instance, if building for Python 2 but loading in Python 3:

```
ImportError: dynamic module does not define init function (PyInit_ycm_core)
```

If building for Python 3 but loading in Python 2:

```
ImportError: dynamic module does not define init function (initycm_core)
```

Setting the `g:icm_server_python_interpreter` option to force the use of a
specific Python interpreter for `ycmd` is usually the easiest way to solve the
problem. Common values for that option are `/usr/bin/python` and
`/usr/bin/python3`.

### I get a linker warning regarding `libpython` on Mac when compiling iCM

If the warning is `ld: warning: path '/usr/lib/libpython2.7.dylib' following -L
not a directory`, then feel free to ignore it; it's caused by a limitation of
CMake and is not an issue. Everything should still work fine.

### I get a weird window at the top of my file when I use the semantic engine

This is Vim's `preview` window. Vim uses it to show you extra information about
something if such information is available. iCM provides Vim with such extra
information. For instance, when you select a function in the completion list,
the `preview` window will hold that function's prototype and the prototypes of
any overloads of the function. It will stay there after you select the
completion so that you can use the information about the parameters and their
types to write the function call.

If you would like this window to auto-close after you select a completion
string, set the `g:icm_autoclose_preview_window_after_completion` option to `1`
in your `vimrc` file. Similarly, the `g:icm_autoclose_preview_window_after_insertion`
option can be set to close the `preview` window after leaving insert mode.

If you don't want this window to ever show up, add `set completeopt-=preview` to
your `vimrc`. Also make sure that the `g:icm_add_preview_to_completeopt` option
is set to `0`.

### It appears that iCM is not working

In Vim, run `:messages` and carefully read the output. iCM will echo messages to
the message log if it encounters problems. It's likely you misconfigured
something and iCM is complaining about it.

Also, you may want to run the `:IcmDebugInfo` command; it will make iCM spew out
various debugging information, including the iCM and [ycmd][] logfile paths and
the compile flags for the current file if the file is a Swift file
and you have compiled in Swift support. Logfiles can be opened in the editor
using [the `:IcmToggleLogs` command](#the-ycmtogglelogs-command).

### Sometimes it takes much longer to get semantic completions than normal

This means that the Swift language facilities (which iCM uses for Swift
semantic completion) failed to pre-compile your file's preamble. In other
words, there was an error compiling some of the source code you pulled in
through your header files. I suggest calling the `:IcmDiags` command to see
what they were.

Bottom line, if Swift can't pre-compile your file's because there
were errors in it, you're going to get slow completions because there's no AST
cache.

### iCM auto-inserts completion strings I don't want!

This means you probably have some mappings that interfere with iCM's internal
ones. Make sure you don't have something mapped to `<C-p>`, `<C-x>` or `<C-u>`
(in insert mode).

iCM _never_ selects something for you; it just shows you a menu and the user has
to explicitly select something. If something is being selected automatically,
this means there's a bug or a misconfiguration somewhere.

### I get a `E227: mapping already exists for <blah>` error when I start Vim

This means that iCM tried to set up a key mapping but failed because you already
had something mapped to that key combination. The `<blah>` part of the message
will tell you what was the key combination that failed.

Look in the _Options_ section and see if any of the default mappings conflict
with your own. Then change that option value to something else so that the
conflict goes away.

### I get `'GLIBC_2.XX' not found (required by libclang.so)` when starting Vim

Your system is too old for the precompiled binaries from llvm.org. Compile
Clang on your machine and then link against the `libclang.so` you just produced.
See the full installation guide for help.

### I'm trying to use a Homebrew Vim with iCM and I'm getting segfaults

Something (I don't know what) is wrong with the way that Homebrew configures and
builds Vim. I recommend using [MacVim][]. Even if you don't like the MacVim GUI,
you can use the Vim binary that is inside the MacVim.app package (it's
`MacVim.app/Contents/MacOS/Vim`) and get the Vim console experience.

### I have a Homebrew Python and/or MacVim; can't compile/SIGABRT when starting

You should probably run `brew rm python; brew install python` to get the latest
fixes that should make iCM work with such a configuration. Also rebuild Macvim
then. If you still get problems with this, see [issue #18][issue18] for
suggestions.

### I get `LONG_BIT definition appears wrong for platform` when compiling

Look at the output of your CMake call. There should be a line in it like the
following (with `.dylib` in place of `.so` on a Mac):

```
-- Found PythonLibs: /usr/lib/libpython2.7.so (Required is at least version "2.5")
```

That would be the **correct** output. An example of **incorrect** output would
be the following:

```
-- Found PythonLibs: /usr/lib/libpython2.7.so (found suitable version "2.5.1", minimum required is "2.5")
```

Notice how there's an extra bit of output there, the `found suitable version
"<version>"` part, where `<version>` is not the same as the version of the
dynamic library. In the example shown, the library is version 2.7 but the second
string is version `2.5.1`.

This means that CMake found one version of Python headers and a different
version for the library. This is wrong. It can happen when you have multiple
versions of Python installed on your machine.

You should probably add the following flags to your cmake call (again, `dylib`
instead of `so` on a Mac):

```
-DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so
```

This will force the paths to the Python include directory and the Python library
to use. You may need to set these flags to something else, but you need to make
sure you use the same version of Python that your Vim binary is built against,
which is highly likely to be the system's default Python.

### I get `libpython2.7.a [...] relocation R_X86_64_32` when compiling

The error is usually encountered when compiling iCM on Centos or RHEL. The full
error looks something like the following:

```
/usr/bin/ld: /usr/local/lib/libpython2.7.a(abstract.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
```

It's possible to get a slightly different error that's similar to the one above.
Here's the problem and how you solve it:

Your `libpython2.7.a` was not compiled with `-fPIC` so it can't be linked into
`ycm_core.so`.  Use the `-DPYTHON_LIBRARY=` CMake flag to point it to a `.so`
version of libpython on your machine (for instance,
`-DPYTHON_LIBRARY=/usr/lib/libpython2.7.so`). Naturally, this means you'll have
to go through the full installation guide by hand.

### I get `Vim: Caught deadly signal SEGV` on Vim startup

This can happen on some Linux distros. If you encounter this situation, run Vim
under `gdb`. You'll probably see something like this in the output when Vim
crashes:

```
undefined symbol: clang_CompileCommands_dispose
```

This means that Vim is trying to load a `libclang.so` that is too old. You need
at least a 3.9 libclang. Just go through the installation guide and make sure
you are using a correct `libclang.so`. We recommend downloading prebuilt
binaries from llvm.org.


### I get `Fatal Python error: PyThreadState_Get: no current thread` on startup

This is caused by linking a static version of `libpython` into ycmd's
`ycm_core.so`.  This leads to multiple copies of the python interpreter loaded
when `python` loads `ycmd_core.so` and this messes up python's global state.
The details aren't important.

The solution is that the version of Python linked and run against must be built
with either `--enable-shared` or `--enable-framework` (on OS X).
This is achieved as follows (**NOTE:** for Mac, replace `--enable-shared`
with `--enable-framework`):

- When building python from source: `./configure --enable-shared {options}`
- When building python from pyenv:
  `PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install {version}`


### `install.py` says python must be compiled with `--enable-framework`. Wat?

See the previous answer for how to ensure your python is built to support
dynamic modules.

### iCM does not read identifiers from my tags files

First, put `let g:icm_collect_identifiers_from_tags_files = 1` in your vimrc.

Make sure you are using [Exuberant Ctags][exuberant-ctags] to produce your tags
files since the only supported tag format is the [Exuberant Ctags
format][ctags-format]. The format from "plain" ctags is NOT supported. The
output of `ctags --version` should list "Exuberant Ctags".

Ctags needs to be called with the `--fields=+l` (that's a lowercase `L`, not a
one) option because iCM needs the `language:<lang>` field in the tags output.

**NOTE:** [Exuberant Ctags][exuberant-ctags] by default sets language tag for
`*.h` files as `C++`. If you have C (not C++) project, consider giving parameter
`--langmap=c:.c.h` to ctags to see tags from `*.h` files.

**NOTE:** Mac OS X comes with "plain" ctags installed by default. `brew install
ctags` will get you the Exuberant Ctags version.

Also make sure that your Vim `tags` option is set correctly. See `:h 'tags'` for
details. If you want to see which tag files iCM will read for a given buffer,
run `:echo tagfiles()` with the relevant buffer active. Note that that function
will only list tag files that already exist.

### `CTRL-U` in insert mode does not work

iCM keeps you in a `completefunc` completion mode when you're typing in insert
mode and Vim disables `<C-U>` in completion mode as a "feature." Sadly there's
nothing I can do about this.

### iCM conflicts with UltiSnips TAB key usage

iCM comes with support for UltiSnips (snippet suggestions in the popup menu),
but you'll have to change the UltiSnips mappings. See `:h UltiSnips-triggers` in
Vim for details. You'll probably want to change some/all of the following
options:

```viml
g:UltiSnipsExpandTrigger
g:UltiSnipsJumpForwardTrigger
g:UltiSnipsJumpBackwardTrigger
```

### Snippets added with `:UltiSnipsAddFiletypes` do not appear in the popup menu

For efficiency, iCM only fetches UltiSnips snippets in specific scenarios like
visiting a buffer or setting its filetype. You can force iCM to retrieve them by
manually triggering the `FileType` autocommand:

```viml
:doautocmd FileType
```

### Why isn't iCM just written in plain VimScript, FFS?

Because of the identifier completion engine and subsequence-based filtering.
Let's say you have _many_ dozens of files open in a single Vim instance (I often
do); the identifier-based engine then needs to store thousands (if not tens of
thousands) of identifiers in its internal data-structures. When the user types,
iCM needs to perform subsequence-based filtering on _all_ of those identifiers
(every single one!) in less than 10 milliseconds.

I'm sorry, but that level of performance is just plain impossible to achieve
with VimScript. I've tried, and the language is just too slow. No, you can't get
acceptable performance even if you limit yourself to just the identifiers in the
current file and simple prefix-based filtering.

### Why does iCM demand such a recent version of Vim?

iCM needs a version of Vim with the timers feature to achieve full
asynchronicity. This feature is available since Vim 7.4.1578.

### Nasty bugs happen if I have the `vim-autoclose` plugin installed

Use the [delimitMate][] plugin instead. It does the same thing without
conflicting with iCM.

### I get an internal compiler error when installing

This can be a problem on virtual servers with limited memory. A possible
solution is to add more swap memory. A more practical solution would be to force
the build script to run only one compile job at a time. You can do this by
setting the `iCM_CORES` environment variable to `1`. Example:

```
iCM_CORES=1 ./install.py --clang-completer
```

### I get weird errors when I press `Ctrl-C` in Vim

_Never_ use `Ctrl-C` in Vim.

Using `Ctrl-C` to exit insert mode in Vim is a bad idea. The main issue here is
that `Ctrl-C` in Vim doesn't just leave insert mode, it leaves it without
triggering `InsertLeave` autocommands (as per Vim docs). This is a bad idea and
is likely to break many other things and not just iCM.

Bottom line, if you use `Ctrl-C` to exit insert mode in Vim, you're gonna have a
bad time.

If pressing `<esc>` is too annoying (agreed, it is), we suggest mapping it to
something more convenient. On a QWERTY keyboard, a good pick for the `<esc>` map
is `inoremap jk <Esc>`. This is right on the home row, it's an incredibly rare
digraph in English and if you ever need to type those two chars in sequence in
insert mode, you just type `j`, then wait 500ms, then type `k`.

### When I start vim I get a runtime error saying `R6034 An application has made an attempt to load the C runtime library incorrectly.`

[CMake and other things seem to screw up the PATH with their own msvcrXX.dll
versions.][identify-R6034-cause] Add the following to the very top of your vimrc
to remove these entries from the path.

```python
python << EOF
import os
import re
path = os.environ['PATH'].split(';')

def contains_msvcr_lib(folder):
    try:
        for item in os.listdir(folder):
            if re.match(r'msvcr\d+\.dll', item):
                return True
    except:
        pass
    return False

path = [folder for folder in path if not contains_msvcr_lib(folder)]
os.environ['PATH'] = ';'.join(path)
EOF
```

### I hear that iCM only supports Python 2, is that true?

**No.** Both the Vim client and the [ycmd server][ycmd] run on Python 2 or 3. If
you work on a Python 3 project, you may need to set `g:icm_python_binary_path`
to the Python interpreter you use for your project to get completions for that
version of Python.

### On Windows I get `E887: Sorry, this command is disabled, the Python's site module could not be loaded`

If you are running vim on Windows with Python 2.7.11, this is likely caused by a
[bug][vim_win-python2.7.11-bug]. Follow this
[workaround][vim_win-python2.7.11-bug_workaround] or use a different version
(Python 2.7.12 does not suffer from the bug).

### I can't complete python packages in a virtual environment.

This means that the Python used to run [JediHTTP][] is not the Python of the
virtual environment you're in. To resolve this you either set
`g:icm_python_binary_path` to the absolute path of the Python binary in your
virtual environment or since virtual environment will put that Python
executable first in your PATH when the virtual environment is active then if
you set `g:icm_python_binary_path` to just `'python'` it will be found as the
first Python and used to run [JediHTTP][].

### I want to defer loading of iCompleteMe until after Vim finishes booting

In recent versions of Vim, you can install iCM in a folder under
`~/.vim/pack/*/opt` and then load it once the user is idle via an autocommand:

```viml
augroup load_ycm
  autocmd!
  autocmd CursorHold, CursorHoldI * :packadd iCompleteMe
                                \ | autocmd! load_ycm
augroup END
```

### iCM does not shut down when I quit Vim

iCM relies on the `VimLeave` event to shut down the [ycmd server][ycmd]. Some
plugins prevent this event from triggering by exiting Vim through an autocommand
without using the `nested` keyword (see `:h autocmd-nested`). One of these
plugins is [vim-nerdtree-tabs][]. You should identify which plugin is
responsible for the issue and report it to the plugin author. Note that when
this happens, [ycmd][] will automatically shut itself down after 30 minutes.

Contributor Code of Conduct
---------------------------

Please note that this project is released with a [Contributor Code of
Conduct][ccoc]. By participating in this project you agree to abide by its
terms.


Contact
-------

If you have bug reports or feature suggestions, please use the [issue
tracker][tracker].

The author's homepage is <http://jerrymarino.com>.

License
-------

This software is licensed under the [GPL v3 license][gpl].
© 2015-2017 YouCompleteMe contributors
© 2017 Jerry Marino

[ycmd]: https://github.com/Valloric/ycmd
[Clang]: http://clang.llvm.org/
[vundle]: https://github.com/VundleVim/Vundle.vim#about
[pathogen]: https://github.com/tpope/vim-pathogen#pathogenvim
[clang-download]: http://llvm.org/releases/download.html
[brew]: http://brew.sh
[cmake-download]: https://cmake.org/download/
[macvim]: https://github.com/macvim-dev/macvim/releases
[vimrc]: http://vimhelp.appspot.com/starting.txt.html#vimrc
[gpl]: http://www.gnu.org/copyleft/gpl.html
[vim]: http://www.vim.org/
[syntastic]: https://github.com/scrooloose/syntastic
[lightline]: https://github.com/itchyny/lightline.vim
[flags_example]: https://github.com/Valloric/ycmd/blob/master/cpp/ycm/.ycm_extra_conf.py
[compdb]: http://clang.llvm.org/docs/JSONCompilationDatabase.html
[subsequence]: https://en.wikipedia.org/wiki/Subsequence
[vim-build]: https://github.com/jerrymarino/iCompleteMe/wiki/Building-Vim-from-source
[tracker]: https://github.com/jerrymarino/iCompleteMe/issues?state=open
[issue18]: https://github.com/jerrymarino/iCompleteMe/issues/18
[delimitMate]: https://github.com/Raimondi/delimitMate
[completer-api]: https://github.com/Valloric/ycmd/blob/master/ycmd/completers/completer.py
[eclim]: http://eclim.org/
[ultisnips]: https://github.com/SirVer/ultisnips/blob/master/doc/UltiSnips.txt
[exuberant-ctags]: http://ctags.sourceforge.net/
[ctags-format]: http://ctags.sourceforge.net/FORMAT
[vundle-bug]: https://github.com/VundleVim/Vundle.vim/issues/48
[status-mes]: https://groups.google.com/forum/#!topic/vim_dev/WeBBjkXE8H8
[python-re]: https://docs.python.org/2/library/re.html#regular-expression-syntax
[Options]: https://github.com/jerrymarino/iCompleteMe#options
[vim-win-download]: https://bintray.com/micbou/generic/vim
[python-win-download]: https://www.python.org/downloads/windows/
[visual-studio-download]: https://www.visualstudio.com/downloads/
[identify-R6034-cause]: http://stackoverflow.com/questions/14552348/runtime-error-r6034-in-embedded-python-application/34696022
[ccoc]: https://github.com/jerrymarino/iCompleteMe/blob/master/CODE_OF_CONDUCT.md
[vim_win-python2.7.11-bug]: https://github.com/vim/vim/issues/717
[vim_win-python2.7.11-bug_workaround]: https://github.com/vim/vim-win32-installer/blob/a27bbdba9bb87fa0e44c8a00d33d46be936822dd/appveyor.bat#L86-L88
[vim-nerdtree-tabs]: https://github.com/jistr/vim-nerdtree-tabs

[SwiftySwiftVim]: https://github.com/jerrymarino/swiftyswiftvim
[YouCompleteMe]: https://github.com/Vallorc/YouCompleteMe
[Valloric]: https://github.com/Vallorc
[iCompleteMe]: https://github.com/jerrymarino/iCompleteMe
[YCM]: https://github.com/Vallorc/YouCompleteMe
[iCM]: https://github.com/jerrymarino/iCompleteMe

