syntax enable


filetype indent on
set autoindent
" show line numbers
set nu
" ........................interface settings...........
"let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
"let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
"colo dues
set background=dark
set t_Co=256
"set termguicolors
"let g:deus_termcolors=256
"set cursorline

call plug#begin('~/.vim/plugged')
Plug 'altercation/vim-colors-solarized'
Plug 'vim-airline/vim-airline'

Plug 'jiangmiao/auto-pairs'


" On-demand loading
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
" Better autocompletion
Plug 'Shougo/neocomplcache.vim'

Plug 'python-mode/python-mode', { 'branch': 'develop' }



" Initialize plugin system
call plug#end()

" NERDTree ----------------------------- 

" toggle nerdtree display
map <F3> :NERDTreeToggle<CR>
" open nerdtree with the current file selected
nmap ,t :NERDTreeFind<CR>
" don;t show these file types
let NERDTreeIgnore = ['\.pyc$', '\.pyo$']

" NeoComplCache ------------------------------

" most of them not documented because I'm not sure how they work
" (docs aren't good, had to do a lot of trial and error to make 
" it play nice)
let g:neocomplcache_enable_at_startup = 1
let g:neocomplcache_enable_ignore_case = 1
let g:neocomplcache_enable_smart_case = 1
let g:neocomplcache_enable_auto_select = 1
let g:neocomplcache_enable_fuzzy_completion = 1
let g:neocomplcache_enable_camel_case_completion = 1
let g:neocomplcache_enable_underbar_completion = 1
let g:neocomplcache_fuzzy_completion_start_length = 1
let g:neocomplcache_auto_completion_start_length = 1
let g:neocomplcache_manual_completion_start_length = 1
let g:neocomplcache_min_keyword_length = 1
let g:neocomplcache_min_syntax_length = 1
" complete with workds from any opened file
let g:neocomplcache_same_filetype_lists = {}
let g:neocomplcache_same_filetype_lists._ = '_'

let g:pymode_run = 1
let g:pymode_run_bind = '<leader>r'
let g:pymode_breakpoint = 1
let g:pymode_breakpoint_bind = '<leader>b'
let g:pymode_breakpoint_cmd = ''
let mapleader = ","




"---------------------------- Python Specific bindings ------------------------------------
let python_highlight_all=1
augroup vimrc_autocmds
	autocmd!
	autocmd FileType python highlight Excess ctermbg=DarkGrey guibg=Black
    autocmd FileType python match Excess /\%80v.*/
    autocmd FileType python set nowrap
	autocmd FileType html hi clear Excess
	autocmd FileType htmldjango hi clear Excess
augroup END
"---------------------------- Python Specific bindings end  ---------------------------------

"---------------------------- Airline Settings --------------------------------------------
let g:airline_powerline_fonts                   = 1
let g:airline#extensions#tabline#enabled        = 1
let g:airline#extensions#syntastic#enabled      = 1
let g:airline#extensions#fugitive#enabled      = 1
let g:airline#extensions#tabline#show_buffers   = 1
"let g:airline#extensions#tabline#show_tab_nr    = 1
let g:airline#extensions#tabline#buffer_nr_show = 1
let g:airline#extensions#tabline#fnamemod       = ':t'
let g:airline_theme='simple'
let g:airline#extensions#virtualenv#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail_improved'
let g:airline_inactive_collapse=1
let g:airline_mode_map = {
            \ '__' : '-',
            \ 'n'  : 'N',
            \ 'i'  : 'I',
            \ 'R'  : 'R',
            \ 'c'  : 'C',
            \ 'v'  : 'V',
            \ 'V'  : 'V',
            \ '' : 'V',
            \ 's'  : 'S',
            \ 'S'  : 'S',
            \ '' : 'S',
            \ }


"---------------------------- Airline Settings End ----------------------------------------
