# a) Install dependencies
opam init --disable-sandboxing
opam switch create . 4.07.1
eval $(opam env)
opam install dune

# b) Run all necessary parts of the codebase
dune build main.exe
dune exec ./main.exe
