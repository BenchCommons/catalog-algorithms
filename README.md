# Hello World 🌍

> "Hello World" in every programming language we can get our hands on.

[![CI](https://github.com/matbrgz/Hello-World/actions/workflows/hello-world.yml/badge.svg)](https://github.com/matbrgz/Hello-World/actions/workflows/hello-world.yml)
![Languages](https://img.shields.io/badge/languages-452-blue)
![Tested in CI](https://img.shields.io/badge/tested%20in%20CI-377%20(83%25)-brightgreen)
![TIOBE coverage](https://img.shields.io/badge/TIOBE%20top%20100-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

Since 1974, when Brian Kernighan used it in *Programming in C: A Tutorial*, printing **Hello World** has been
the first program almost everyone writes in a new language. This repository collects that program in
**452 languages**: every language in the [TIOBE Index](https://www.tiobe.com/tiobe-index/) top 100,
the languages that shaped computing history, the new languages people are talking about, Brazilian languages,
and a long tail of assembly, shell, scientific, hardware, markup and esoteric languages.

**377 of 452 programs (83%) are checked on every push** by GitHub Actions on Linux, macOS and Windows:

- ✅ **346 run** and their output is checked to contain "Hello World";
- 🔧 **31 are compiled or validated** with the language's official tool, for languages that cannot print text
  (shaders, smart contracts, hardware, configuration) or have no free runtime.

## Contents

- [TIOBE Index — Top 50](#tiobe-index--top-50)
- [TIOBE Index — 51 to 100](#tiobe-index--51-to-100)
- [Historical languages](#historical-languages)
- [Modern & trending languages](#modern--trending-languages)
- [More general-purpose languages](#more-general-purpose-languages)
- [Assembly, IR & bytecode](#assembly-ir--bytecode)
- [Shells & automation](#shells--automation)
- [Scientific, math & statistics](#scientific-math--statistics)
- [Query languages](#query-languages)
- [Hardware, GPU & quantum](#hardware-gpu--quantum)
- [Smart contracts](#smart-contracts)
- [Game & embedded scripting](#game--embedded-scripting)
- [Markup, templates & web](#markup-templates--web)
- [Configuration, build & infrastructure](#configuration-build--infrastructure)
- [Brazilian languages 🇧🇷](#brazilian-languages-)
- [Esoteric languages](#esoteric-languages)
- [Running the tests](#running-the-tests)
- [Contributing](#contributing)

## TIOBE Index — Top 50

Ranking from the TIOBE Index of **September 2026**. Rankings change every month; the list is a snapshot. Purely graphical languages (Scratch, LabVIEW, Ladder Logic) have no text syntax, so their files contain a textual representation.

| # | Language | File | CI | Notes |
|---|---|---|---|---|
| 1 | **Python** | [`HelloWorld.py`](languages/python/HelloWorld.py) | ✅ |  |
| 2 | **C** | [`HelloWorld.c`](languages/c/HelloWorld.c) | ✅ |  |
| 3 | **C++** | [`HelloWorld.cpp`](languages/cpp/HelloWorld.cpp) | ✅ |  |
| 4 | **Java** | [`HelloWorld.java`](languages/java/HelloWorld.java) | ✅ |  |
| 5 | **C#** | [`HelloWorld.cs`](languages/c-sharp/HelloWorld.cs) | ✅ |  |
| 6 | **JavaScript** | [`HelloWorld.js`](languages/javascript/HelloWorld.js) | ✅ |  |
| 7 | **Visual Basic** | [`HelloWorld.vb`](languages/visual-basic/HelloWorld.vb) | ✅ |  |
| 8 | **SQL** | [`HelloWorld.sql`](languages/sql/HelloWorld.sql) | ✅ |  |
| 9 | **R** | [`HelloWorld.r`](languages/r/HelloWorld.r) | ✅ |  |
| 10 | **Rust** | [`HelloWorld.rs`](languages/rust/HelloWorld.rs) | ✅ |  |
| 11 | **Fortran** | [`HelloWorld.f90`](languages/fortran/HelloWorld.f90) | ✅ |  |
| 12 | **Go** | [`HelloWorld.go`](languages/go/HelloWorld.go) | ✅ |  |
| 13 | **Delphi / Object Pascal** | [`HelloWorld.dpr`](languages/delphi/HelloWorld.dpr) | ✅ |  |
| 14 | **PHP** | [`HelloWorld.php`](languages/php/HelloWorld.php) | ✅ |  |
| 15 | **Scratch** | [`HelloWorld.txt`](languages/scratch/HelloWorld.txt) |  | textual (scratchblocks) form |
| 16 | **Assembly language** | [`HelloWorld.asm`](languages/assembly-x86-dos/HelloWorld.asm) | ✅ | MASM/TASM, DOS `int 21h` |
| 17 | **Ada** | [`helloworld.adb`](languages/ada/helloworld.adb) | ✅ |  |
| 18 | **Swift** | [`HelloWorld.swift`](languages/swift/HelloWorld.swift) | ✅ |  |
| 19 | **Objective-C** | [`HelloWorld.m`](languages/objective-c/HelloWorld.m) | ✅ |  |
| 20 | **COBOL** | [`HelloWorld.cob`](languages/cobol/HelloWorld.cob) | ✅ |  |
| 21 | **Julia** | [`HelloWorld.jl`](languages/julia/HelloWorld.jl) | ✅ |  |
| 22 | **Ruby** | [`HelloWorld.rb`](languages/ruby/HelloWorld.rb) | ✅ |  |
| 23 | **Perl** | [`HelloWorld.pl`](languages/perl/HelloWorld.pl) | ✅ |  |
| 24 | **SAS** | [`HelloWorld.sas`](languages/sas/HelloWorld.sas) |  |  |
| 25 | **Classic Visual Basic** | [`HelloWorld.bas`](languages/visual-basic-6/HelloWorld.bas) |  |  |
| 26 | **Kotlin** | [`HelloWorld.kt`](languages/kotlin/HelloWorld.kt) | ✅ |  |
| 27 | **MATLAB** | [`HelloWorld.m`](languages/matlab/HelloWorld.m) | ✅ | also runs in GNU Octave |
| 28 | **Caml** | [`HelloWorld.ml`](languages/caml/HelloWorld.ml) | ✅ |  |
| 29 | **Prolog** | [`HelloWorld.pro`](languages/prolog/HelloWorld.pro) | ✅ |  |
| 30 | **GML** | [`HelloWorld.gml`](languages/gml/HelloWorld.gml) |  |  |
| 31 | **Lua** | [`HelloWorld.lua`](languages/lua/HelloWorld.lua) | ✅ |  |
| 32 | **PowerShell** | [`HelloWorld.ps1`](languages/powershell/HelloWorld.ps1) | ✅ |  |
| 33 | **D** | [`HelloWorld.d`](languages/d/HelloWorld.d) | ✅ |  |
| 34 | **PL/SQL** | [`HelloWorld.pls`](languages/pl-sql/HelloWorld.pls) | ✅ |  |
| 35 | **ABAP** | [`HelloWorld.abap`](languages/abap/HelloWorld.abap) | ✅ |  |
| 36 | **Transact-SQL** | [`HelloWorld.sql`](languages/transact-sql/HelloWorld.sql) | ✅ |  |
| 37 | **VBScript** | [`HelloWorld.vbs`](languages/vbscript/HelloWorld.vbs) | ✅ |  |
| 38 | **OCaml** | [`HelloWorld.ml`](languages/ocaml/HelloWorld.ml) | ✅ |  |
| 39 | **TypeScript** | [`HelloWorld.ts`](languages/typescript/HelloWorld.ts) | ✅ |  |
| 40 | **Zig** | [`HelloWorld.zig`](languages/zig/HelloWorld.zig) | ✅ |  |
| 41 | **Dart** | [`HelloWorld.dart`](languages/dart/HelloWorld.dart) | ✅ |  |
| 42 | **X++** | [`HelloWorld.xpp`](languages/x-plus-plus/HelloWorld.xpp) |  |  |
| 43 | **Lisp** | [`HelloWorld.lisp`](languages/common-lisp/HelloWorld.lisp) | ✅ |  |
| 44 | **Scala** | [`HelloWorld.scala`](languages/scala/HelloWorld.scala) | ✅ |  |
| 45 | **LabVIEW** | [`HelloWorld.txt`](languages/labview/HelloWorld.txt) |  | graphical; textual description |
| 46 | **Ladder Logic** | [`HelloWorld.txt`](languages/ladder-logic/HelloWorld.txt) |  | graphical; ASCII rung |
| 47 | **VHDL** | [`HelloWorld.vhd`](languages/vhdl/HelloWorld.vhd) | ✅ |  |
| 48 | **XSLT** | [`HelloWorld.xsl`](languages/xslt/HelloWorld.xsl) | ✅ |  |
| 49 | **Haskell** | [`HelloWorld.hs`](languages/haskell/HelloWorld.hs) | ✅ |  |
| 50 | **(Visual) FoxPro** | [`HelloWorld.prg`](languages/foxpro/HelloWorld.prg) |  |  |

## TIOBE Index — 51 to 100

TIOBE publishes positions 51–100 unranked, in alphabetical order.

| Language | File | CI | Notes |
|---|---|---|---|
| **ActionScript** | [`HelloWorld.as`](languages/actionscript/HelloWorld.as) |  |  |
| **Apex** | [`HelloWorld.cls`](languages/apex/HelloWorld.cls) |  |  |
| **AppleScript** | [`HelloWorld.applescript`](languages/applescript/HelloWorld.applescript) | ✅ |  |
| **Awk** | [`HelloWorld.awk`](languages/awk/HelloWorld.awk) | ✅ |  |
| **Bash** | [`HelloWorld.bash`](languages/bash/HelloWorld.bash) | ✅ |  |
| **bc** | [`HelloWorld.bc`](languages/bc/HelloWorld.bc) | ✅ |  |
| **BCPL** | [`HelloWorld.bcpl`](languages/bcpl/HelloWorld.bcpl) | ✅ |  |
| **Bourne shell** | [`HelloWorld.sh`](languages/bourne-shell/HelloWorld.sh) | ✅ |  |
| **C shell** | [`HelloWorld.csh`](languages/c-shell/HelloWorld.csh) | ✅ |  |
| **CFML** | [`HelloWorld.cfm`](languages/cfml/HelloWorld.cfm) | ✅ |  |
| **CL (OS/400)** | [`HelloWorld.clle`](languages/cl-os400/HelloWorld.clle) |  |  |
| **Clojure** | [`HelloWorld.clj`](languages/clojure/HelloWorld.clj) | ✅ |  |
| **CoffeeScript** | [`HelloWorld.coffee`](languages/coffeescript/HelloWorld.coffee) | ✅ |  |
| **cT** | [`HelloWorld.t`](languages/ct/HelloWorld.t) |  |  |
| **ECMAScript** | [`HelloWorld.mjs`](languages/ecmascript/HelloWorld.mjs) | ✅ |  |
| **EGL** | [`HelloWorld.egl`](languages/egl/HelloWorld.egl) |  |  |
| **Elixir** | [`HelloWorld.exs`](languages/elixir/HelloWorld.exs) | ✅ |  |
| **Erlang** | [`helloworld.erl`](languages/erlang/helloworld.erl) | ✅ |  |
| **F#** | [`HelloWorld.fs`](languages/f-sharp/HelloWorld.fs) | ✅ |  |
| **GAMS** | [`HelloWorld.gms`](languages/gams/HelloWorld.gms) |  |  |
| **Groovy** | [`HelloWorld.groovy`](languages/groovy/HelloWorld.groovy) | ✅ |  |
| **Io** | [`HelloWorld.io`](languages/io/HelloWorld.io) | ✅ |  |
| **J** | [`HelloWorld.ijs`](languages/j/HelloWorld.ijs) | ✅ |  |
| **J#** | [`HelloWorld.jsl`](languages/j-sharp/HelloWorld.jsl) |  |  |
| **JScript** | [`HelloWorld.js`](languages/jscript/HelloWorld.js) | ✅ | Windows Script Host |
| **Logo** | [`HelloWorld.logo`](languages/logo/HelloWorld.logo) | ✅ |  |
| **ML** | [`HelloWorld.sml`](languages/standard-ml/HelloWorld.sml) | ✅ |  |
| **MS-DOS batch** | [`HelloWorld.bat`](languages/batch/HelloWorld.bat) | ✅ |  |
| **NetLogo** | [`HelloWorld.nls`](languages/netlogo/HelloWorld.nls) |  |  |
| **Nim** | [`HelloWorld.nim`](languages/nim/HelloWorld.nim) | ✅ |  |
| **OpenCL** | [`HelloWorld.cl`](languages/opencl/HelloWorld.cl) | 🔧 |  |
| **PL/I** | [`HelloWorld.pli`](languages/pl-i/HelloWorld.pli) | ✅ |  |
| **PowerScript** | [`HelloWorld.powerscript`](languages/powerscript/HelloWorld.powerscript) |  |  |
| **Pure Data** | [`HelloWorld.pd`](languages/pure-data/HelloWorld.pd) | ✅ | patch file; prints to the Pd console |
| **PureBasic** | [`HelloWorld.pb`](languages/purebasic/HelloWorld.pb) |  |  |
| **Q** | [`HelloWorld.q`](languages/q/HelloWorld.q) |  |  |
| **REBOL** | [`HelloWorld.reb`](languages/rebol/HelloWorld.reb) | ✅ |  |
| **Ring** | [`HelloWorld.ring`](languages/ring/HelloWorld.ring) | ✅ |  |
| **Scheme** | [`HelloWorld.scm`](languages/scheme/HelloWorld.scm) | ✅ |  |
| **Solidity** | [`HelloWorld.sol`](languages/solidity/HelloWorld.sol) | 🔧 |  |
| **Structured Text** | [`HelloWorld.st`](languages/structured-text/HelloWorld.st) | 🔧 | IEC 61131-3 |
| **Tcl** | [`HelloWorld.tcl`](languages/tcl/HelloWorld.tcl) | ✅ |  |
| **tcsh** | [`HelloWorld.tcsh`](languages/tcsh/HelloWorld.tcsh) | ✅ |  |
| **thinBasic** | [`HelloWorld.tbasic`](languages/thinbasic/HelloWorld.tbasic) |  |  |
| **V** | [`HelloWorld.v`](languages/v/HelloWorld.v) |  |  |
| **Xbase++** | [`HelloWorld.prg`](languages/xbase-plus-plus/HelloWorld.prg) | ✅ |  |
| **XC** | [`HelloWorld.xc`](languages/xc/HelloWorld.xc) | ✅ |  |
| **Xojo** | [`HelloWorld.xojo_code`](languages/xojo/HelloWorld.xojo_code) |  |  |
| **XPL** | [`HelloWorld.xpl`](languages/xpl/HelloWorld.xpl) |  |  |
| **Z shell** | [`HelloWorld.zsh`](languages/z-shell/HelloWorld.zsh) | ✅ |  |

## Historical languages

Languages that shaped programming, ordered by the year they first appeared.

| Language | Year | File | CI | Notes |
|---|---|---|---|---|
| **MAD** | 1959 | [`HELLO.mad`](languages/mad/HELLO.mad) |  | Michigan Algorithm Decoder |
| **RPG** | 1959 | [`HelloWorld.rpgle`](languages/rpg/HelloWorld.rpgle) |  | modern free-form RPG IV |
| **ALGOL 60** | 1960 | [`HelloWorld.alg`](languages/algol-60/HelloWorld.alg) | ✅ |  |
| **JOSS** | 1963 | [`HelloWorld.joss`](languages/joss/HelloWorld.joss) |  |  |
| **BASIC** | 1964 | [`HelloWorld.bas`](languages/basic/HelloWorld.bas) | ✅ |  |
| **JCL** | 1964 | [`HELLO.jcl`](languages/jcl/HELLO.jcl) |  | IBM mainframe Job Control Language |
| **ALGOL W** | 1966 | [`HelloWorld.alw`](languages/algol-w/HelloWorld.alw) | ✅ |  |
| **APL** | 1966 | [`HelloWorld.apl`](languages/apl/HelloWorld.apl) | ✅ |  |
| **MUMPS (M)** | 1966 | [`HelloWorld.m`](languages/mumps/HelloWorld.m) | ✅ |  |
| **Simula** | 1967 | [`HelloWorld.sim`](languages/simula/HelloWorld.sim) | ✅ |  |
| **SNOBOL4** | 1967 | [`HelloWorld.sno`](languages/snobol4/HelloWorld.sno) | ✅ |  |
| **ALGOL 68** | 1968 | [`HelloWorld.a68`](languages/algol-68/HelloWorld.a68) | ✅ |  |
| **FOCAL** | 1968 | [`HelloWorld.foc`](languages/focal/HelloWorld.foc) | ✅ |  |
| **B** | 1969 | [`HelloWorld.b`](languages/b/HelloWorld.b) | ✅ |  |
| **Forth** | 1970 | [`HelloWorld.fth`](languages/forth/HelloWorld.fth) | ✅ |  |
| **Pascal** | 1970 | [`HelloWorld.pas`](languages/pascal/HelloWorld.pas) | ✅ |  |
| **INTERCAL** | 1972 | [`HelloWorld.i`](languages/intercal/HelloWorld.i) | ✅ |  |
| **Smalltalk** | 1972 | [`HelloWorld.st`](languages/smalltalk/HelloWorld.st) | ✅ |  |
| **COMAL** | 1973 | [`HelloWorld.lst`](languages/comal/HelloWorld.lst) | ✅ |  |
| **Ratfor** | 1974 | [`HelloWorld.r`](languages/ratfor/HelloWorld.r) | ✅ |  |
| **CLU** | 1975 | [`HelloWorld.clu`](languages/clu/HelloWorld.clu) |  |  |
| **Commodore BASIC** | 1977 | [`HelloWorld.bas`](languages/commodore-basic/HelloWorld.bas) | ✅ |  |
| **Icon** | 1977 | [`HelloWorld.icn`](languages/icon/HelloWorld.icn) | ✅ |  |
| **Hope** | 1978 | [`HelloWorld.hop`](languages/hope/HelloWorld.hop) | ✅ |  |
| **Modula-2** | 1978 | [`HelloWorld.mod`](languages/modula-2/HelloWorld.mod) | ✅ |  |
| **dBase** | 1979 | [`HelloWorld.prg`](languages/dbase/HelloWorld.prg) | ✅ |  |
| **REXX** | 1979 | [`HelloWorld.rexx`](languages/rexx/HelloWorld.rexx) | ✅ |  |
| **BBC BASIC** | 1981 | [`HelloWorld.bbc`](languages/bbc-basic/HelloWorld.bbc) | ✅ |  |
| **PostScript** | 1982 | [`HelloWorld.ps`](languages/postscript/HelloWorld.ps) | ✅ |  |
| **Turing** | 1982 | [`HelloWorld.t`](languages/turing/HelloWorld.t) |  |  |
| **occam** | 1983 | [`HelloWorld.occ`](languages/occam/HelloWorld.occ) |  |  |
| **Standard ML** | 1983 | [`HelloWorld.sml`](languages/standard-ml/HelloWorld.sml) | ✅ |  |
| **Verilog / SystemVerilog** | 1984 | [`HelloWorld.sv`](languages/verilog/HelloWorld.sv) | ✅ |  |
| **Clipper** | 1985 | [`HelloWorld.prg`](languages/clipper/HelloWorld.prg) | ✅ |  |
| **Miranda** | 1985 | [`HelloWorld.mira`](languages/miranda/HelloWorld.mira) | ✅ |  |
| **Eiffel** | 1986 | [`hello_world.e`](languages/eiffel/hello_world.e) | ✅ |  |
| **ABC** | 1987 | [`HelloWorld.abc`](languages/abc/HelloWorld.abc) | ✅ |  |
| **HyperTalk** | 1987 | [`HelloWorld.hypertalk`](languages/hypertalk/HelloWorld.hypertalk) |  |  |
| **Oberon** | 1987 | [`HelloWorld.Mod`](languages/oberon/HelloWorld.Mod) | ✅ |  |
| **Self** | 1987 | [`HelloWorld.self`](languages/self/HelloWorld.self) |  |  |
| **Lingo** | 1988 | [`HelloWorld.ls`](languages/lingo/HelloWorld.ls) |  |  |
| **Modula-3** | 1988 | [`Main.m3`](languages/modula-3/Main.m3) | ✅ |  |
| **Sather** | 1990 | [`HelloWorld.sa`](languages/sather/HelloWorld.sa) |  |  |
| **TI-BASIC** | 1990 | [`HELLO.8xp.txt`](languages/ti-basic/HELLO.8xp.txt) |  | TI-83/84 calculators |
| **QBasic** | 1991 | [`HELLO.BAS`](languages/qbasic/HELLO.BAS) | ✅ |  |
| **NewtonScript** | 1993 | [`HelloWorld.nwt`](languages/newtonscript/HelloWorld.nwt) | ✅ |  |
| **Limbo** | 1995 | [`HelloWorld.b`](languages/limbo/HelloWorld.b) |  |  |
| **LotusScript** | 1995 | [`HelloWorld.lss`](languages/lotusscript/HelloWorld.lss) |  |  |
| **Python 2** | 2000 | [`HelloWorld.py`](languages/python-2/HelloWorld.py) | ✅ |  |

## Modern & trending languages

New or fast-growing languages that are not (yet) in the TIOBE top 100.

| Language | File | CI | Notes |
|---|---|---|---|
| **Ballerina** | [`HelloWorld.bal`](languages/ballerina/HelloWorld.bal) | ✅ |  |
| **Bend** | [`HelloWorld.bend`](languages/bend/HelloWorld.bend) | ✅ |  |
| **C3** | [`HelloWorld.c3`](languages/c3/HelloWorld.c3) | ✅ |  |
| **Carbon** | [`HelloWorld.carbon`](languages/carbon/HelloWorld.carbon) | ✅ | experimental |
| **Chapel** | [`HelloWorld.chpl`](languages/chapel/HelloWorld.chpl) | ✅ |  |
| **Crystal** | [`HelloWorld.cr`](languages/crystal/HelloWorld.cr) | ✅ |  |
| **Elm** | [`Main.elm`](languages/elm/Main.elm) | 🔧 |  |
| **Gleam** | [`HelloWorld.gleam`](languages/gleam/HelloWorld.gleam) | ✅ |  |
| **Grain** | [`HelloWorld.gr`](languages/grain/HelloWorld.gr) | ✅ |  |
| **Hare** | [`HelloWorld.ha`](languages/hare/HelloWorld.ha) | ✅ |  |
| **Haxe** | [`HelloWorld.hx`](languages/haxe/HelloWorld.hx) | ✅ |  |
| **Inko** | [`HelloWorld.inko`](languages/inko/HelloWorld.inko) | ✅ |  |
| **Jai** | [`HelloWorld.jai`](languages/jai/HelloWorld.jai) |  | closed beta |
| **Koka** | [`helloworld.kk`](languages/koka/helloworld.kk) | ✅ |  |
| **Lean 4** | [`HelloWorld.lean`](languages/lean/HelloWorld.lean) | ✅ |  |
| **Mojo** | [`HelloWorld.mojo`](languages/mojo/HelloWorld.mojo) | ✅ |  |
| **MoonBit** | [`HelloWorld.mbt`](languages/moonbit/HelloWorld.mbt) | ✅ |  |
| **Odin** | [`HelloWorld.odin`](languages/odin/HelloWorld.odin) | ✅ |  |
| **Pony** | [`HelloWorld.pony`](languages/pony/HelloWorld.pony) | ✅ |  |
| **Q#** | [`HelloWorld.qs`](languages/q-sharp/HelloWorld.qs) | ✅ |  |
| **Racket** | [`HelloWorld.rkt`](languages/racket/HelloWorld.rkt) | ✅ |  |
| **Raku (Perl 6)** | [`HelloWorld.raku`](languages/raku/HelloWorld.raku) | ✅ |  |
| **ReScript** | [`HelloWorld.res`](languages/rescript/HelloWorld.res) | ✅ |  |
| **Roc** | [`HelloWorld.roc`](languages/roc/HelloWorld.roc) | ✅ |  |
| **Unison** | [`HelloWorld.u`](languages/unison/HelloWorld.u) | ✅ |  |
| **Vala** | [`HelloWorld.vala`](languages/vala/HelloWorld.vala) | ✅ |  |
| **WebAssembly (WAT)** | [`HelloWorld.wat`](languages/webassembly/HelloWorld.wat) | ✅ |  |

## More general-purpose languages

Functional, logic, object-oriented and scripting languages outside the TIOBE top 100.

| Language | File | CI | Notes |
|---|---|---|---|
| **Agda** | [`HelloWorld.agda`](languages/agda/HelloWorld.agda) | ✅ |  |
| **Alice ML** | [`HelloWorld.aml`](languages/alice-ml/HelloWorld.aml) |  |  |
| **Arc** | [`HelloWorld.arc`](languages/arc/HelloWorld.arc) | ✅ |  |
| **AssemblyScript** | [`HelloWorld.ts`](languages/assemblyscript/HelloWorld.ts) | ✅ |  |
| **ATS** | [`HelloWorld.dats`](languages/ats/HelloWorld.dats) | ✅ |  |
| **Austral** | [`HelloWorld.aum`](languages/austral/HelloWorld.aum) | ✅ |  |
| **AutoLISP** | [`HelloWorld.lsp`](languages/autolisp/HelloWorld.lsp) |  |  |
| **Babashka** | [`HelloWorld.bb`](languages/babashka/HelloWorld.bb) | ✅ |  |
| **Beef** | [`Program.bf`](languages/beef/Program.bf) |  |  |
| **Berry** | [`HelloWorld.be`](languages/berry/HelloWorld.be) | ✅ |  |
| **Boo** | [`HelloWorld.boo`](languages/boo/HelloWorld.boo) | ✅ |  |
| **Carp** | [`HelloWorld.carp`](languages/carp/HelloWorld.carp) | ✅ |  |
| **Ceylon** | [`run.ceylon`](languages/ceylon/run.ceylon) | ✅ |  |
| **CHICKEN Scheme** | [`HelloWorld.scm`](languages/chicken-scheme/HelloWorld.scm) | ✅ |  |
| **Civet** | [`HelloWorld.civet`](languages/civet/HelloWorld.civet) | ✅ |  |
| **Clean** | [`HelloWorld.icl`](languages/clean/HelloWorld.icl) | ✅ |  |
| **ClojureScript** | [`HelloWorld.cljs`](languages/clojurescript/HelloWorld.cljs) | ✅ |  |
| **Cobra** | [`HelloWorld.cobra`](languages/cobra/HelloWorld.cobra) | ✅ |  |
| **COOL** | [`HelloWorld.cl`](languages/cool/HelloWorld.cl) |  | Classroom Object Oriented Language; two variants |
| **Cpp2 (cppfront)** | [`HelloWorld.cpp2`](languages/cppfront/HelloWorld.cpp2) | ✅ |  |
| **Curry** | [`HelloWorld.curry`](languages/curry/HelloWorld.curry) | ✅ |  |
| **Cyclone** | [`HelloWorld.cyc`](languages/cyclone/HelloWorld.cyc) |  |  |
| **Dafny** | [`HelloWorld.dfy`](languages/dafny/HelloWorld.dfy) | ✅ |  |
| **Dylan** | [`hello-world.dylan`](languages/dylan/hello-world.dylan) | ✅ |  |
| **Emacs Lisp** | [`HelloWorld.el`](languages/emacs-lisp/HelloWorld.el) | ✅ |  |
| **Eta** | [`Main.hs`](languages/eta/Main.hs) | ✅ |  |
| **Euphoria** | [`HelloWorld.ex`](languages/euphoria/HelloWorld.ex) | ✅ |  |
| **F*** | [`HelloWorld.fst`](languages/fstar/HelloWorld.fst) | 🔧 |  |
| **Factor** | [`hello-world.factor`](languages/factor/hello-world.factor) | ✅ |  |
| **Fantom** | [`HelloWorld.fan`](languages/fantom/HelloWorld.fan) | ✅ |  |
| **Fennel** | [`HelloWorld.fnl`](languages/fennel/HelloWorld.fnl) | ✅ |  |
| **FreeBASIC** | [`HelloWorld.bas`](languages/freebasic/HelloWorld.bas) | ✅ |  |
| **Frege** | [`HelloWorld.fr`](languages/frege/HelloWorld.fr) | ✅ |  |
| **G-Portugol** | [`HelloWorld.gpt`](languages/g-portugol/HelloWorld.gpt) | ✅ | open source Portugol compiler, 2005 |
| **Genie** | [`HelloWorld.gs`](languages/genie/HelloWorld.gs) | ✅ |  |
| **Golo** | [`HelloWorld.golo`](languages/golo/HelloWorld.golo) | ✅ |  |
| **Gosu** | [`HelloWorld.gsp`](languages/gosu/HelloWorld.gsp) | ✅ |  |
| **Hack** | [`HelloWorld.hack`](languages/hack/HelloWorld.hack) | ✅ |  |
| **HolyC** | [`HelloWorld.HC`](languages/holyc/HelloWorld.HC) | ✅ |  |
| **Hy** | [`HelloWorld.hy`](languages/hy/HelloWorld.hy) | ✅ |  |
| **Hylo** | [`HelloWorld.hylo`](languages/hylo/HelloWorld.hylo) | ✅ |  |
| **Idris** | [`HelloWorld.idr`](languages/idris/HelloWorld.idr) | ✅ |  |
| **Imba** | [`HelloWorld.imba`](languages/imba/HelloWorld.imba) | ✅ |  |
| **Jakt** | [`HelloWorld.jakt`](languages/jakt/HelloWorld.jakt) |  |  |
| **Janet** | [`HelloWorld.janet`](languages/janet/HelloWorld.janet) | ✅ |  |
| **Joy** | [`HelloWorld.joy`](languages/joy/HelloWorld.joy) | ✅ |  |
| **Juliar** | [`HelloWorld.jrl`](languages/juliar/HelloWorld.jrl) |  |  |
| **Kotlin Script** | [`HelloWorld.main.kts`](languages/kotlin-script/HelloWorld.main.kts) | ✅ |  |
| **LFE** | [`HelloWorld.lfe`](languages/lfe/HelloWorld.lfe) | ✅ |  |
| **LiveScript** | [`HelloWorld.ls`](languages/livescript/HelloWorld.ls) | ✅ |  |
| **Lobster** | [`HelloWorld.lobster`](languages/lobster/HelloWorld.lobster) | ✅ |  |
| **Logtalk** | [`hello_world.lgt`](languages/logtalk/hello_world.lgt) | ✅ |  |
| **Mercury** | [`helloworld.m`](languages/mercury/helloworld.m) | ✅ |  |
| **MoonScript** | [`HelloWorld.moon`](languages/moonscript/HelloWorld.moon) | ✅ |  |
| **Nelua** | [`HelloWorld.nelua`](languages/nelua/HelloWorld.nelua) | ✅ |  |
| **Nemerle** | [`HelloWorld.n`](languages/nemerle/HelloWorld.n) |  |  |
| **NetRexx** | [`HelloWorld.nrx`](languages/netrexx/HelloWorld.nrx) | ✅ |  |
| **newLISP** | [`HelloWorld.lsp`](languages/newlisp/HelloWorld.lsp) | ✅ |  |
| **Objective-J** | [`HelloWorld.j`](languages/objective-j/HelloWorld.j) | ✅ |  |
| **Oxygene** | [`HelloWorld.pas`](languages/oxygene/HelloWorld.pas) |  |  |
| **Oz** | [`HelloWorld.oz`](languages/oz/HelloWorld.oz) | ✅ |  |
| **Pawn** | [`HelloWorld.pwn`](languages/pawn/HelloWorld.pwn) | ✅ |  |
| **Picat** | [`hello_world.pi`](languages/picat/hello_world.pi) | ✅ |  |
| **PicoLisp** | [`HelloWorld.l`](languages/picolisp/HelloWorld.l) | ✅ |  |
| **Pike** | [`HelloWorld.pike`](languages/pike/HelloWorld.pike) | ✅ |  |
| **Portugol (VisuAlg)** | [`HelloWorld.alg`](languages/visualg/HelloWorld.alg) | ✅ | pseudocode used to teach programming in Brazil |
| **Portugol Studio** | [`HelloWorld.por`](languages/portugol-studio/HelloWorld.por) | ✅ | UNIVALI |
| **Potigol** | [`HelloWorld.poti`](languages/potigol/HelloWorld.poti) | ✅ | IFRN, functional language in Portuguese |
| **Processing** | [`HelloWorld.pde`](languages/processing/HelloWorld.pde) | ✅ |  |
| **PureScript** | [`Main.purs`](languages/purescript/Main.purs) | ✅ |  |
| **ReasonML** | [`HelloWorld.re`](languages/reasonml/HelloWorld.re) | ✅ |  |
| **Red** | [`HelloWorld.red`](languages/red/HelloWorld.red) | ✅ |  |
| **Rocq (Coq)** | [`HelloWorld.v`](languages/coq/HelloWorld.v) | ✅ |  |
| **Seed7** | [`HelloWorld.sd7`](languages/seed7/HelloWorld.sd7) | ✅ |  |
| **Shen** | [`HelloWorld.shen`](languages/shen/HelloWorld.shen) | ✅ |  |
| **Small Basic** | [`HelloWorld.sb`](languages/small-basic/HelloWorld.sb) |  |  |
| **Terra** | [`HelloWorld.t`](languages/terra/HelloWorld.t) | ✅ |  |
| **Toit** | [`hello.toit`](languages/toit/hello.toit) | ✅ |  |
| **Umka** | [`HelloWorld.um`](languages/umka/HelloWorld.um) | ✅ |  |
| **Unicon** | [`HelloWorld.icn`](languages/unicon/HelloWorld.icn) | ✅ |  |
| **Vale** | [`HelloWorld.vale`](languages/vale/HelloWorld.vale) | ✅ |  |
| **Wren** | [`HelloWorld.wren`](languages/wren/HelloWorld.wren) | ✅ |  |
| **X10** | [`HelloWorld.x10`](languages/x10/HelloWorld.x10) | ✅ |  |
| **Xtend** | [`HelloWorld.xtend`](languages/xtend/HelloWorld.xtend) | ✅ |  |
| **Zephir** | [`World.zep`](languages/zephir/World.zep) | ✅ |  |
| **Égua / Delégua** | [`HelloWorld.egua`](languages/egua/HelloWorld.egua) | ✅ | Delégua is a fork of Égua and runs `.egua` files |

## Assembly, IR & bytecode

Machine-level languages for specific architectures and virtual machines.

| Language | File | CI | Notes |
|---|---|---|---|
| **Assembly (6502, Commodore 64)** | [`HelloWorld.asm`](languages/assembly-6502/HelloWorld.asm) | 🔧 | 64tass syntax; `SYS 49152` to run |
| **Assembly (ARM64, Linux)** | [`HelloWorld.s`](languages/assembly-arm64-linux/HelloWorld.s) | ✅ |  |
| **Assembly (ARM64, macOS)** | [`HelloWorld.s`](languages/assembly-arm64-macos/HelloWorld.s) | ✅ |  |
| **Assembly (MIPS, SPIM/MARS)** | [`HelloWorld.asm`](languages/assembly-mips/HelloWorld.asm) | ✅ |  |
| **Assembly (RISC-V, Linux)** | [`HelloWorld.s`](languages/assembly-risc-v/HelloWorld.s) | ✅ |  |
| **Assembly (x86-64, Linux, NASM)** | [`HelloWorld.asm`](languages/assembly-x86-64-linux/HelloWorld.asm) | ✅ |  |
| **Assembly (Z80, CP/M)** | [`HELLO.ASM`](languages/assembly-z80/HELLO.ASM) | ✅ |  |
| **C--** | [`HelloWorld.cmm`](languages/c-minus-minus/HelloWorld.cmm) |  |  |
| **CIL (.NET IL)** | [`HelloWorld.il`](languages/cil/HelloWorld.il) | ✅ |  |
| **JVM bytecode (Jasmin)** | [`HelloWorld.j`](languages/jasmin/HelloWorld.j) | ✅ |  |
| **LLVM IR** | [`HelloWorld.ll`](languages/llvm-ir/HelloWorld.ll) | ✅ |  |
| **MMIX** | [`HelloWorld.mms`](languages/mmix/HelloWorld.mms) | ✅ | Donald Knuth's architecture from *The Art of Computer Programming* |

## Shells & automation

Command shells, OS scripting and desktop automation.

| Language | File | CI | Notes |
|---|---|---|---|
| **AutoHotkey** | [`HelloWorld.ahk`](languages/autohotkey/HelloWorld.ahk) |  |  |
| **AutoIt** | [`HelloWorld.au3`](languages/autoit/HelloWorld.au3) |  |  |
| **Dash** | [`HelloWorld.sh`](languages/dash/HelloWorld.sh) | ✅ |  |
| **dc** | [`HelloWorld.dc`](languages/dc/HelloWorld.dc) | ✅ |  |
| **Elvish** | [`HelloWorld.elv`](languages/elvish/HelloWorld.elv) | ✅ |  |
| **Expect** | [`HelloWorld.exp`](languages/expect/HelloWorld.exp) | ✅ |  |
| **fish** | [`HelloWorld.fish`](languages/fish/HelloWorld.fish) | ✅ |  |
| **Google Apps Script** | [`Code.gs`](languages/google-apps-script/Code.gs) |  |  |
| **JavaScript for Automation (JXA)** | [`HelloWorld.js`](languages/jxa/HelloWorld.js) | ✅ |  |
| **jq** | [`HelloWorld.jq`](languages/jq/HelloWorld.jq) | ✅ |  |
| **KiXtart** | [`HelloWorld.kix`](languages/kixtart/HelloWorld.kix) |  |  |
| **Korn shell** | [`HelloWorld.ksh`](languages/korn-shell/HelloWorld.ksh) | ✅ |  |
| **LibreOffice Basic** | [`HelloWorld.bas`](languages/libreoffice-basic/HelloWorld.bas) |  |  |
| **m4** | [`HelloWorld.m4`](languages/m4/HelloWorld.m4) | ✅ |  |
| **mIRC scripting** | [`HelloWorld.mrc`](languages/mirc-script/HelloWorld.mrc) |  |  |
| **Nushell** | [`HelloWorld.nu`](languages/nushell/HelloWorld.nu) | ✅ |  |
| **rc (Plan 9 shell)** | [`HelloWorld.rc`](languages/rc/HelloWorld.rc) | ✅ |  |
| **sed** | [`HelloWorld.sed`](languages/sed/HelloWorld.sed) | ✅ |  |
| **VBA** | [`HelloWorld.bas`](languages/vba/HelloWorld.bas) |  | Microsoft Office macros |
| **Vim script** | [`HelloWorld.vim`](languages/vim-script/HelloWorld.vim) | ✅ |  |
| **Windows CMD (NT batch)** | [`HelloWorld.cmd`](languages/cmd/HelloWorld.cmd) | ✅ |  |
| **Xonsh** | [`HelloWorld.xsh`](languages/xonsh/HelloWorld.xsh) | ✅ |  |
| **YSH (Oils)** | [`HelloWorld.ysh`](languages/ysh/HelloWorld.ysh) | ✅ |  |

## Scientific, math & statistics

Numerical computing, computer algebra and statistics.

| Language | File | CI | Notes |
|---|---|---|---|
| **AMPL** | [`HelloWorld.run`](languages/ampl/HelloWorld.run) | ✅ |  |
| **BQN** | [`HelloWorld.bqn`](languages/bqn/HelloWorld.bqn) | ✅ |  |
| **GAP** | [`HelloWorld.g`](languages/gap/HelloWorld.g) | ✅ |  |
| **GAUSS** | [`HelloWorld.gss`](languages/gauss/HelloWorld.gss) |  |  |
| **GNU Octave** | [`HelloWorld.m`](languages/gnu-octave/HelloWorld.m) | ✅ |  |
| **gnuplot** | [`HelloWorld.gp`](languages/gnuplot/HelloWorld.gp) | ✅ |  |
| **IDL** | [`HelloWorld.pro`](languages/idl/HelloWorld.pro) | ✅ |  |
| **K** | [`HelloWorld.k`](languages/k/HelloWorld.k) | ✅ |  |
| **Macaulay2** | [`HelloWorld.m2`](languages/macaulay2/HelloWorld.m2) | ✅ |  |
| **Magma** | [`HelloWorld.m`](languages/magma/HelloWorld.m) |  |  |
| **Maple** | [`HelloWorld.mpl`](languages/maple/HelloWorld.mpl) |  |  |
| **Maxima** | [`HelloWorld.mac`](languages/maxima/HelloWorld.mac) | ✅ |  |
| **MiniZinc** | [`HelloWorld.mzn`](languages/minizinc/HelloWorld.mzn) | ✅ |  |
| **Modelica** | [`HelloWorld.mo`](languages/modelica/HelloWorld.mo) | ✅ |  |
| **Nial** | [`HelloWorld.ndf`](languages/nial/HelloWorld.ndf) | ✅ |  |
| **PARI/GP** | [`HelloWorld.gp`](languages/pari-gp/HelloWorld.gp) | ✅ |  |
| **REDUCE** | [`HelloWorld.red`](languages/reduce/HelloWorld.red) | ✅ |  |
| **SageMath** | [`HelloWorld.sage`](languages/sagemath/HelloWorld.sage) | ✅ |  |
| **Scilab** | [`HelloWorld.sce`](languages/scilab/HelloWorld.sce) | ✅ |  |
| **SPSS Syntax** | [`HelloWorld.sps`](languages/spss/HelloWorld.sps) | ✅ |  |
| **Stan** | [`HelloWorld.stan`](languages/stan/HelloWorld.stan) | ✅ |  |
| **Stata** | [`HelloWorld.do`](languages/stata/HelloWorld.do) |  |  |
| **Uiua** | [`HelloWorld.ua`](languages/uiua/HelloWorld.ua) | ✅ |  |
| **Wolfram Language (Mathematica)** | [`HelloWorld.wl`](languages/wolfram/HelloWorld.wl) | ✅ |  |

## Query languages

Databases, graphs and data querying.

| Language | File | CI | Notes |
|---|---|---|---|
| **Cypher** | [`HelloWorld.cypher`](languages/cypher/HelloWorld.cypher) | ✅ |  |
| **Datalog (Soufflé)** | [`HelloWorld.dl`](languages/souffle/HelloWorld.dl) | ✅ |  |
| **DAX** | [`HelloWorld.dax`](languages/dax/HelloWorld.dax) |  |  |
| **Excel formula** | [`HelloWorld.xlsx.txt`](languages/excel/HelloWorld.xlsx.txt) | ✅ | type it into any cell |
| **GraphQL** | [`HelloWorld.graphql`](languages/graphql/HelloWorld.graphql) | 🔧 | schema plus query; the resolver returns "Hello World" |
| **KQL (Kusto)** | [`HelloWorld.kql`](languages/kql/HelloWorld.kql) |  |  |
| **Natural** | [`HELLO.nsp`](languages/natural/HELLO.nsp) |  |  |
| **OpenEdge ABL (Progress 4GL)** | [`HelloWorld.p`](languages/openedge-abl/HelloWorld.p) |  |  |
| **PL/pgSQL** | [`HelloWorld.sql`](languages/pl-pgsql/HelloWorld.sql) | ✅ |  |
| **Power Query M** | [`HelloWorld.pq`](languages/power-query-m/HelloWorld.pq) |  |  |
| **SPARQL** | [`HelloWorld.rq`](languages/sparql/HelloWorld.rq) | ✅ |  |
| **Splunk SPL** | [`HelloWorld.spl`](languages/splunk-spl/HelloWorld.spl) |  |  |
| **SQLite SQL** | [`HelloWorld.sql`](languages/sqlite/HelloWorld.sql) | ✅ |  |
| **XQuery** | [`HelloWorld.xq`](languages/xquery/HelloWorld.xq) | ✅ |  |

## Hardware, GPU & quantum

Hardware description, GPU kernels and quantum programs.

| Language | File | CI | Notes |
|---|---|---|---|
| **Amaranth HDL** | [`hello_world.py`](languages/amaranth/hello_world.py) | ✅ |  |
| **Bluespec SystemVerilog** | [`HelloWorld.bsv`](languages/bluespec/HelloWorld.bsv) | ✅ |  |
| **Chisel** | [`HelloWorld.scala`](languages/chisel/HelloWorld.scala) | 🔧 |  |
| **CUDA** | [`HelloWorld.cu`](languages/cuda/HelloWorld.cu) | 🔧 |  |
| **GLSL** | [`HelloWorld.comp`](languages/glsl/HelloWorld.comp) | 🔧 | Vulkan compute shader with `debugPrintfEXT` |
| **HLSL** | [`HelloWorld.hlsl`](languages/hlsl/HelloWorld.hlsl) | 🔧 |  |
| **Metal Shading Language** | [`HelloWorld.metal`](languages/metal/HelloWorld.metal) |  |  |
| **OpenQASM** | [`HelloWorld.qasm`](languages/openqasm/HelloWorld.qasm) | 🔧 | quantum circuit; no text output |
| **SystemC** | [`HelloWorld.cpp`](languages/systemc/HelloWorld.cpp) | ✅ |  |
| **WGSL** | [`HelloWorld.wgsl`](languages/wgsl/HelloWorld.wgsl) | 🔧 | no text output; renders a solid color |

## Smart contracts

Blockchain and smart-contract languages.

| Language | File | CI | Notes |
|---|---|---|---|
| **Cairo** | [`hello_world.cairo`](languages/cairo/hello_world.cairo) | ✅ |  |
| **Clarity** | [`hello-world.clar`](languages/clarity/hello-world.clar) | 🔧 |  |
| **ink! (Rust)** | [`lib.rs`](languages/ink/lib.rs) | 🔧 |  |
| **Michelson (Tezos)** | [`hello_world.tz`](languages/michelson/hello_world.tz) | ✅ |  |
| **Move** | [`hello_world.move`](languages/move/hello_world.move) | 🔧 |  |
| **Sway (Fuel)** | [`main.sw`](languages/sway/main.sw) | 🔧 |  |
| **Vyper** | [`HelloWorld.vy`](languages/vyper/HelloWorld.vy) | 🔧 |  |
| **Yul** | [`HelloWorld.yul`](languages/yul/HelloWorld.yul) | 🔧 |  |

## Game & embedded scripting

Languages embedded in game engines and applications.

| Language | File | CI | Notes |
|---|---|---|---|
| **AGS Script (Adventure Game Studio)** | [`GlobalScript.asc`](languages/ags-script/GlobalScript.asc) |  |  |
| **AngelScript** | [`HelloWorld.as`](languages/angelscript/HelloWorld.as) | ✅ |  |
| **Arduino** | [`HelloWorld.ino`](languages/arduino/HelloWorld.ino) | 🔧 |  |
| **BlitzBasic** | [`HelloWorld.bb`](languages/blitzbasic/HelloWorld.bb) |  |  |
| **ChaiScript** | [`HelloWorld.chai`](languages/chaiscript/HelloWorld.chai) | ✅ |  |
| **GDScript (Godot)** | [`hello_world.gd`](languages/gdscript/hello_world.gd) | ✅ |  |
| **Gravity** | [`HelloWorld.gravity`](languages/gravity/HelloWorld.gravity) | ✅ |  |
| **Inform 7** | [`story.ni`](languages/inform-7/story.ni) | ✅ |  |
| **LSL (Second Life)** | [`HelloWorld.lsl`](languages/lsl/HelloWorld.lsl) | 🔧 |  |
| **Luau (Roblox)** | [`HelloWorld.luau`](languages/luau/HelloWorld.luau) | ✅ |  |
| **MicroPython** | [`main.py`](languages/micropython/main.py) | ✅ |  |
| **Minecraft function** | [`hello.mcfunction`](languages/mcfunction/hello.mcfunction) | 🔧 |  |
| **Papyrus (Skyrim)** | [`HelloWorld.psc`](languages/papyrus/HelloWorld.psc) |  |  |
| **PICO-8 Lua** | [`hello.p8.lua`](languages/pico-8/hello.p8.lua) |  |  |
| **QuakeC** | [`progs.qc`](languages/quakec/progs.qc) | 🔧 |  |
| **Ren'Py** | [`script.rpy`](languages/renpy/script.rpy) | 🔧 |  |
| **Squirrel** | [`HelloWorld.nut`](languages/squirrel/HelloWorld.nut) | ✅ |  |
| **Teal** | [`HelloWorld.tl`](languages/teal/HelloWorld.tl) | ✅ |  |
| **UnrealScript** | [`HelloWorld.uc`](languages/unrealscript/HelloWorld.uc) |  |  |
| **YueScript** | [`HelloWorld.yue`](languages/yuescript/HelloWorld.yue) | ✅ |  |
| **ZIL (Zork Implementation Language)** | [`hello.zil`](languages/zil/hello.zil) | ✅ |  |

## Markup, templates & web

Documents, stylesheets and templates. They render or produce "Hello World" instead of printing it.

| Language | File | CI | Notes |
|---|---|---|---|
| **AsciiDoc** | [`HelloWorld.adoc`](languages/asciidoc/HelloWorld.adoc) | ✅ |  |
| **Astro** | [`HelloWorld.astro`](languages/astro/HelloWorld.astro) | ✅ |  |
| **Blade (Laravel)** | [`hello.blade.php`](languages/blade/hello.blade.php) | ✅ |  |
| **Classic ASP** | [`HelloWorld.asp`](languages/asp-classic/HelloWorld.asp) |  |  |
| **CSS** | [`HelloWorld.css`](languages/css/HelloWorld.css) | 🔧 |  |
| **EJS** | [`HelloWorld.ejs`](languages/ejs/HelloWorld.ejs) | ✅ |  |
| **Encapsulated PostScript** | [`HelloWorld.eps`](languages/postscript-eps/HelloWorld.eps) | ✅ |  |
| **ERB (Embedded Ruby)** | [`HelloWorld.erb`](languages/erb/HelloWorld.erb) | ✅ |  |
| **Graphviz DOT** | [`HelloWorld.dot`](languages/graphviz-dot/HelloWorld.dot) | 🔧 |  |
| **Haml** | [`HelloWorld.haml`](languages/haml/HelloWorld.haml) | ✅ |  |
| **Handlebars** | [`HelloWorld.hbs`](languages/handlebars/HelloWorld.hbs) | 🔧 |  |
| **HTML** | [`HelloWorld.html`](languages/html/HelloWorld.html) | ✅ |  |
| **Jinja** | [`HelloWorld.jinja`](languages/jinja/HelloWorld.jinja) | ✅ |  |
| **JSP** | [`HelloWorld.jsp`](languages/jsp/HelloWorld.jsp) | ✅ |  |
| **JSX (React)** | [`HelloWorld.jsx`](languages/jsx/HelloWorld.jsx) | ✅ |  |
| **LaTeX** | [`HelloWorld.tex`](languages/latex/HelloWorld.tex) | ✅ |  |
| **Liquid** | [`HelloWorld.liquid`](languages/liquid/HelloWorld.liquid) | ✅ |  |
| **Markdown** | [`HelloWorld.md`](languages/markdown/HelloWorld.md) | ✅ |  |
| **MDX** | [`HelloWorld.mdx`](languages/mdx/HelloWorld.mdx) | ✅ |  |
| **Mermaid** | [`HelloWorld.mmd`](languages/mermaid/HelloWorld.mmd) | 🔧 |  |
| **Mustache** | [`HelloWorld.mustache`](languages/mustache/HelloWorld.mustache) | ✅ |  |
| **Org mode** | [`HelloWorld.org`](languages/org-mode/HelloWorld.org) | ✅ |  |
| **PlantUML** | [`HelloWorld.puml`](languages/plantuml/HelloWorld.puml) | ✅ |  |
| **Pug** | [`HelloWorld.pug`](languages/pug/HelloWorld.pug) | ✅ |  |
| **Razor (ASP.NET)** | [`HelloWorld.cshtml`](languages/razor/HelloWorld.cshtml) | ✅ |  |
| **reStructuredText** | [`HelloWorld.rst`](languages/restructuredtext/HelloWorld.rst) | ✅ |  |
| **RTF** | [`HelloWorld.rtf`](languages/rtf/HelloWorld.rtf) | ✅ |  |
| **Slim** | [`HelloWorld.slim`](languages/slim/HelloWorld.slim) | ✅ |  |
| **Svelte** | [`HelloWorld.svelte`](languages/svelte/HelloWorld.svelte) | ✅ |  |
| **SVG** | [`HelloWorld.svg`](languages/svg/HelloWorld.svg) | ✅ |  |
| **TeX (plain)** | [`HelloWorld.tex`](languages/tex/HelloWorld.tex) | ✅ |  |
| **troff / groff** | [`HelloWorld.ms`](languages/troff/HelloWorld.ms) | ✅ |  |
| **Twig** | [`HelloWorld.twig`](languages/twig/HelloWorld.twig) | ✅ |  |
| **Typst** | [`HelloWorld.typ`](languages/typst/HelloWorld.typ) | ✅ |  |
| **VRML** | [`HelloWorld.wrl`](languages/vrml/HelloWorld.wrl) | 🔧 |  |
| **Vue (SFC)** | [`HelloWorld.vue`](languages/vue/HelloWorld.vue) | ✅ |  |
| **XML** | [`HelloWorld.xml`](languages/xml/HelloWorld.xml) | ✅ |  |

## Configuration, build & infrastructure

Build systems, configuration languages and infrastructure as code.

| Language | File | CI | Notes |
|---|---|---|---|
| **Ansible** | [`hello-world.yml`](languages/ansible/hello-world.yml) | ✅ |  |
| **Apache Ant** | [`build.xml`](languages/ant/build.xml) | ✅ |  |
| **Bicep** | [`main.bicep`](languages/bicep/main.bicep) | 🔧 |  |
| **CMake** | [`HelloWorld.cmake`](languages/cmake/HelloWorld.cmake) | ✅ |  |
| **CUE** | [`HelloWorld.cue`](languages/cue/HelloWorld.cue) | ✅ |  |
| **Dhall** | [`HelloWorld.dhall`](languages/dhall/HelloWorld.dhall) | ✅ |  |
| **Dockerfile** | [`Dockerfile`](languages/dockerfile/Dockerfile) | ✅ |  |
| **GitHub Actions** | [`hello-world.yml`](languages/github-actions/hello-world.yml) | 🔧 |  |
| **Gradle Kotlin DSL** | [`build.gradle.kts`](languages/gradle-kotlin-dsl/build.gradle.kts) | ✅ |  |
| **HCL (Terraform)** | [`main.tf`](languages/hcl/main.tf) | ✅ |  |
| **JSON** | [`hello.json`](languages/json/hello.json) | ✅ |  |
| **Jsonnet** | [`HelloWorld.jsonnet`](languages/jsonnet/HelloWorld.jsonnet) | ✅ |  |
| **just** | [`justfile`](languages/just/justfile) | ✅ |  |
| **KCL** | [`HelloWorld.k`](languages/kcl/HelloWorld.k) | ✅ |  |
| **Make** | [`Makefile`](languages/make/Makefile) | ✅ |  |
| **Meson** | [`meson.build`](languages/meson/meson.build) | ✅ |  |
| **Nickel** | [`HelloWorld.ncl`](languages/nickel/HelloWorld.ncl) | ✅ |  |
| **Nix** | [`HelloWorld.nix`](languages/nix/HelloWorld.nix) | ✅ |  |
| **Pkl** | [`HelloWorld.pkl`](languages/pkl/HelloWorld.pkl) | ✅ |  |
| **Puppet** | [`hello_world.pp`](languages/puppet/hello_world.pp) | ✅ |  |
| **Rego (Open Policy Agent)** | [`hello.rego`](languages/rego/hello.rego) | ✅ |  |
| **Starlark (Bazel)** | [`BUILD.bazel`](languages/bazel-starlark/BUILD.bazel) | ✅ |  |
| **TOML** | [`hello.toml`](languages/toml/hello.toml) | ✅ |  |
| **YAML** | [`hello.yaml`](languages/yaml/hello.yaml) | ✅ |  |

## Brazilian languages 🇧🇷

Languages created in Brazil or designed for programming in Portuguese. Some of them also appear in other tables.

| Language | File | CI | Notes |
|---|---|---|---|
| **BIRL** | [`HelloWorld.birl`](languages/birl/HelloWorld.birl) | ✅ | keywords from bodybuilder Bambam's catchphrases |
| **Elixir** | [`HelloWorld.exs`](languages/elixir/HelloWorld.exs) | ✅ | created by José Valim, 2012 |
| **G-Portugol** | [`HelloWorld.gpt`](languages/g-portugol/HelloWorld.gpt) | ✅ | open source Portugol compiler, 2005 |
| **Lua** | [`HelloWorld.lua`](languages/lua/HelloWorld.lua) | ✅ | PUC-Rio, 1993 — the most widely used Brazilian language |
| **Portugol (VisuAlg)** | [`HelloWorld.alg`](languages/visualg/HelloWorld.alg) | ✅ | pseudocode used to teach programming in Brazil |
| **Portugol Studio** | [`HelloWorld.por`](languages/portugol-studio/HelloWorld.por) | ✅ | UNIVALI |
| **Potigol** | [`HelloWorld.poti`](languages/potigol/HelloWorld.poti) | ✅ | IFRN, functional language in Portuguese |
| **Égua / Delégua** | [`HelloWorld.egua`](languages/egua/HelloWorld.egua) | ✅ | Delégua is a fork of Égua and runs `.egua` files |

## Esoteric languages

Languages designed as jokes, puzzles or experiments.

| Language | File | CI | Notes |
|---|---|---|---|
| **ArnoldC** | [`HelloWorld.arnoldc`](languages/arnoldc/HelloWorld.arnoldc) | ✅ |  |
| **Befunge** | [`HelloWorld.bf93`](languages/befunge/HelloWorld.bf93) | ✅ |  |
| **BIRL** | [`HelloWorld.birl`](languages/birl/HelloWorld.birl) | ✅ | keywords from bodybuilder Bambam's catchphrases |
| **Brainfuck** | [`HelloWorld.bf`](languages/brainfuck/HelloWorld.bf) | ✅ |  |
| **Chef** | [`HelloWorld.chef`](languages/chef/HelloWorld.chef) | ✅ |  |
| **COW** | [`HelloWorld.cow`](languages/cow/HelloWorld.cow) | ✅ | generated from the Brainfuck program |
| **Emojicode** | [`HelloWorld.emojic`](languages/emojicode/HelloWorld.emojic) | ✅ |  |
| **FALSE** | [`HelloWorld.f`](languages/false/HelloWorld.f) |  |  |
| **GolfScript** | [`HelloWorld.gs`](languages/golfscript/HelloWorld.gs) | ✅ |  |
| **HQ9+** | [`HelloWorld.hq9`](languages/hq9-plus/HelloWorld.hq9) | ✅ | `H` prints "Hello, world!" |
| **LOLCODE** | [`HelloWorld.lol`](languages/lolcode/HelloWorld.lol) | ✅ |  |
| **Ook!** | [`HelloWorld.ook`](languages/ook/HelloWorld.ook) | ✅ | generated from the Brainfuck program |
| **Piet** | [`HelloWorld.txt`](languages/piet/HelloWorld.txt) |  | image-based; link to the canonical program |
| **Pyth** | [`HelloWorld.pyth`](languages/pyth/HelloWorld.pyth) | ✅ |  |
| **Rockstar** | [`HelloWorld.rock`](languages/rockstar/HelloWorld.rock) | ✅ |  |
| **Shakespeare** | [`HelloWorld.spl`](languages/shakespeare/HelloWorld.spl) | ✅ |  |
| **Unlambda** | [`HelloWorld.unl`](languages/unlambda/HelloWorld.unl) | ✅ |  |
| **Whitespace** | [`HelloWorld.ws`](languages/whitespace/HelloWorld.ws) | ✅ |  |

## Running the tests

```sh
python3 scripts/hello.py check              # metadata, files and README are consistent
python3 scripts/hello.py test               # run every language whose toolchain is installed locally
python3 scripts/hello.py test --lang python --lang rust
python3 scripts/hello.py test --changed-since origin/master   # only languages changed on this branch
python3 scripts/hello.py readme             # regenerate this README from languages/*/meta.json
```

## Contributing

1. Check the tables above: is the language already covered?
2. Create a folder `languages/<slug>/` (lowercase, hyphens) with:
   - the program, usually named `HelloWorld.<extension>`;
   - a `meta.json`, for example:
     ```json
     {
       "name": "Python",
       "files": ["HelloWorld.py"],
       "section": "general",
       "notes": "",
       "test": {"group": "base", "run": "python3 HelloWorld.py"}
     }
     ```
     `section` is one of: `historical`, `modern`, `general`, `assembly`, `shells`, `scientific`, `query`, `hardware`, `blockchain`, `game`, `markup`, `config`, `esoteric`.
     `test` is optional: add it when the language can run on a GitHub runner. `group` is `base` (tools preinstalled
     on Ubuntu), `apt` (with an `"apt": ["package"]` list), `extra` (tools set up in the workflow), `macos` or
     `windows`, or `docker` (with a pinned `"image"`; `run` executes inside it). `needs` lists the commands that must
     exist (defaults to the first word of `run`). Set `"kind": "compile"` when the program cannot print and the test
     only checks that the official tool accepts it.
3. The program should print (or display) `Hello World` and be the idiomatic, minimal version for that language.
4. Run `python3 scripts/hello.py readme` and `python3 scripts/hello.py check`, then open a pull request.

## Contributors

Maintained by [@matbrgz](https://github.com/matbrgz).

[![matbrgz](https://github.com/matbrgz.png?size=64)](https://github.com/matbrgz)

[![Contributors](https://contrib.rocks/image?repo=matbrgz/Hello-World)](https://github.com/matbrgz/Hello-World/graphs/contributors)

## License

[MIT](LICENSE)
