# catalog-algorithms

> Classic algorithm implementations across programming languages, measured by the
> [BenchCommons](https://github.com/BenchCommons) toolset. It starts with Hello World in 452 languages.

[![CI](https://github.com/BenchCommons/catalog-algorithms/actions/workflows/hello-world.yml/badge.svg)](https://github.com/BenchCommons/catalog-algorithms/actions/workflows/hello-world.yml)
![Languages](https://img.shields.io/badge/languages-452-blue)
![Tested in CI](https://img.shields.io/badge/tested%20in%20CI-377%20(83%25)-brightgreen)
![TIOBE coverage](https://img.shields.io/badge/TIOBE%20top%20100-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

This repository is the BenchCommons catalog of **classic algorithm implementations across languages**:
n-body, fannkuch-redux, spectral-norm, binary-trees, mandelbrot, sorting, searching, hashing and others.
Every implementation uses a pinned toolchain and has its output checked against a canonical expected output
before it is measured for time, memory and energy with [perfratio](https://github.com/BenchCommons/perfratio)
through [benchmark-tool](https://github.com/BenchCommons/benchmark-tool). The roadmap is tracked in
[issue #11](https://github.com/BenchCommons/catalog-algorithms/issues/11) and in [`docs/specs/`](docs/specs/ROADMAP.md).

It starts from **Hello World**, the first program almost everyone writes in a new language since Brian Kernighan
used it in 1974. Hello World does almost no work, so it is the **startup-cost baseline** for each language:
the time and memory a toolchain needs before any algorithm runs. The catalog has it in **452 languages**:
every language in the [TIOBE Index](https://www.tiobe.com/tiobe-index/) top 100, the languages that shaped
computing history, the new languages people are talking about, Brazilian languages, and a long tail of assembly,
shell, scientific, hardware, markup and esoteric languages.

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
| 1 | **Python** | [`HelloWorld.py`](languages/python/hello-world/HelloWorld.py) | ✅ |  |
| 2 | **C** | [`HelloWorld.c`](languages/c/hello-world/HelloWorld.c) | ✅ |  |
| 3 | **C++** | [`HelloWorld.cpp`](languages/cpp/hello-world/HelloWorld.cpp) | ✅ |  |
| 4 | **Java** | [`HelloWorld.java`](languages/java/hello-world/HelloWorld.java) | ✅ |  |
| 5 | **C#** | [`HelloWorld.cs`](languages/c-sharp/hello-world/HelloWorld.cs) | ✅ |  |
| 6 | **JavaScript** | [`HelloWorld.js`](languages/javascript/hello-world/HelloWorld.js) | ✅ |  |
| 7 | **Visual Basic** | [`HelloWorld.vb`](languages/visual-basic/hello-world/HelloWorld.vb) | ✅ |  |
| 8 | **SQL** | [`HelloWorld.sql`](languages/sql/hello-world/HelloWorld.sql) | ✅ |  |
| 9 | **R** | [`HelloWorld.r`](languages/r/hello-world/HelloWorld.r) | ✅ |  |
| 10 | **Rust** | [`HelloWorld.rs`](languages/rust/hello-world/HelloWorld.rs) | ✅ |  |
| 11 | **Fortran** | [`HelloWorld.f90`](languages/fortran/hello-world/HelloWorld.f90) | ✅ |  |
| 12 | **Go** | [`HelloWorld.go`](languages/go/hello-world/HelloWorld.go) | ✅ |  |
| 13 | **Delphi / Object Pascal** | [`HelloWorld.dpr`](languages/delphi/hello-world/HelloWorld.dpr) | ✅ |  |
| 14 | **PHP** | [`HelloWorld.php`](languages/php/hello-world/HelloWorld.php) | ✅ |  |
| 15 | **Scratch** | [`HelloWorld.txt`](languages/scratch/hello-world/HelloWorld.txt) |  | textual (scratchblocks) form |
| 16 | **Assembly language** | [`HelloWorld.asm`](languages/assembly-x86-dos/hello-world/HelloWorld.asm) | ✅ | MASM/TASM, DOS `int 21h` |
| 17 | **Ada** | [`helloworld.adb`](languages/ada/hello-world/helloworld.adb) | ✅ |  |
| 18 | **Swift** | [`HelloWorld.swift`](languages/swift/hello-world/HelloWorld.swift) | ✅ |  |
| 19 | **Objective-C** | [`HelloWorld.m`](languages/objective-c/hello-world/HelloWorld.m) | ✅ |  |
| 20 | **COBOL** | [`HelloWorld.cob`](languages/cobol/hello-world/HelloWorld.cob) | ✅ |  |
| 21 | **Julia** | [`HelloWorld.jl`](languages/julia/hello-world/HelloWorld.jl) | ✅ |  |
| 22 | **Ruby** | [`HelloWorld.rb`](languages/ruby/hello-world/HelloWorld.rb) | ✅ |  |
| 23 | **Perl** | [`HelloWorld.pl`](languages/perl/hello-world/HelloWorld.pl) | ✅ |  |
| 24 | **SAS** | [`HelloWorld.sas`](languages/sas/hello-world/HelloWorld.sas) |  |  |
| 25 | **Classic Visual Basic** | [`HelloWorld.bas`](languages/visual-basic-6/hello-world/HelloWorld.bas) |  |  |
| 26 | **Kotlin** | [`HelloWorld.kt`](languages/kotlin/hello-world/HelloWorld.kt) | ✅ |  |
| 27 | **MATLAB** | [`HelloWorld.m`](languages/matlab/hello-world/HelloWorld.m) | ✅ | also runs in GNU Octave |
| 28 | **Caml** | [`HelloWorld.ml`](languages/caml/hello-world/HelloWorld.ml) | ✅ |  |
| 29 | **Prolog** | [`HelloWorld.pro`](languages/prolog/hello-world/HelloWorld.pro) | ✅ |  |
| 30 | **GML** | [`HelloWorld.gml`](languages/gml/hello-world/HelloWorld.gml) |  |  |
| 31 | **Lua** | [`HelloWorld.lua`](languages/lua/hello-world/HelloWorld.lua) | ✅ |  |
| 32 | **PowerShell** | [`HelloWorld.ps1`](languages/powershell/hello-world/HelloWorld.ps1) | ✅ |  |
| 33 | **D** | [`HelloWorld.d`](languages/d/hello-world/HelloWorld.d) | ✅ |  |
| 34 | **PL/SQL** | [`HelloWorld.pls`](languages/pl-sql/hello-world/HelloWorld.pls) | ✅ |  |
| 35 | **ABAP** | [`HelloWorld.abap`](languages/abap/hello-world/HelloWorld.abap) | ✅ |  |
| 36 | **Transact-SQL** | [`HelloWorld.sql`](languages/transact-sql/hello-world/HelloWorld.sql) | ✅ |  |
| 37 | **VBScript** | [`HelloWorld.vbs`](languages/vbscript/hello-world/HelloWorld.vbs) | ✅ |  |
| 38 | **OCaml** | [`HelloWorld.ml`](languages/ocaml/hello-world/HelloWorld.ml) | ✅ |  |
| 39 | **TypeScript** | [`HelloWorld.ts`](languages/typescript/hello-world/HelloWorld.ts) | ✅ |  |
| 40 | **Zig** | [`HelloWorld.zig`](languages/zig/hello-world/HelloWorld.zig) | ✅ |  |
| 41 | **Dart** | [`HelloWorld.dart`](languages/dart/hello-world/HelloWorld.dart) | ✅ |  |
| 42 | **X++** | [`HelloWorld.xpp`](languages/x-plus-plus/hello-world/HelloWorld.xpp) |  |  |
| 43 | **Lisp** | [`HelloWorld.lisp`](languages/common-lisp/hello-world/HelloWorld.lisp) | ✅ |  |
| 44 | **Scala** | [`HelloWorld.scala`](languages/scala/hello-world/HelloWorld.scala) | ✅ |  |
| 45 | **LabVIEW** | [`HelloWorld.txt`](languages/labview/hello-world/HelloWorld.txt) |  | graphical; textual description |
| 46 | **Ladder Logic** | [`HelloWorld.txt`](languages/ladder-logic/hello-world/HelloWorld.txt) |  | graphical; ASCII rung |
| 47 | **VHDL** | [`HelloWorld.vhd`](languages/vhdl/hello-world/HelloWorld.vhd) | ✅ |  |
| 48 | **XSLT** | [`HelloWorld.xsl`](languages/xslt/hello-world/HelloWorld.xsl) | ✅ |  |
| 49 | **Haskell** | [`HelloWorld.hs`](languages/haskell/hello-world/HelloWorld.hs) | ✅ |  |
| 50 | **(Visual) FoxPro** | [`HelloWorld.prg`](languages/foxpro/hello-world/HelloWorld.prg) |  |  |

## TIOBE Index — 51 to 100

TIOBE publishes positions 51–100 unranked, in alphabetical order.

| Language | File | CI | Notes |
|---|---|---|---|
| **ActionScript** | [`HelloWorld.as`](languages/actionscript/hello-world/HelloWorld.as) |  |  |
| **Apex** | [`HelloWorld.cls`](languages/apex/hello-world/HelloWorld.cls) |  |  |
| **AppleScript** | [`HelloWorld.applescript`](languages/applescript/hello-world/HelloWorld.applescript) | ✅ |  |
| **Awk** | [`HelloWorld.awk`](languages/awk/hello-world/HelloWorld.awk) | ✅ |  |
| **Bash** | [`HelloWorld.bash`](languages/bash/hello-world/HelloWorld.bash) | ✅ |  |
| **bc** | [`HelloWorld.bc`](languages/bc/hello-world/HelloWorld.bc) | ✅ |  |
| **BCPL** | [`HelloWorld.bcpl`](languages/bcpl/hello-world/HelloWorld.bcpl) | ✅ |  |
| **Bourne shell** | [`HelloWorld.sh`](languages/bourne-shell/hello-world/HelloWorld.sh) | ✅ |  |
| **C shell** | [`HelloWorld.csh`](languages/c-shell/hello-world/HelloWorld.csh) | ✅ |  |
| **CFML** | [`HelloWorld.cfm`](languages/cfml/hello-world/HelloWorld.cfm) | ✅ |  |
| **CL (OS/400)** | [`HelloWorld.clle`](languages/cl-os400/hello-world/HelloWorld.clle) |  |  |
| **Clojure** | [`HelloWorld.clj`](languages/clojure/hello-world/HelloWorld.clj) | ✅ |  |
| **CoffeeScript** | [`HelloWorld.coffee`](languages/coffeescript/hello-world/HelloWorld.coffee) | ✅ |  |
| **cT** | [`HelloWorld.t`](languages/ct/hello-world/HelloWorld.t) |  |  |
| **ECMAScript** | [`HelloWorld.mjs`](languages/ecmascript/hello-world/HelloWorld.mjs) | ✅ |  |
| **EGL** | [`HelloWorld.egl`](languages/egl/hello-world/HelloWorld.egl) |  |  |
| **Elixir** | [`HelloWorld.exs`](languages/elixir/hello-world/HelloWorld.exs) | ✅ |  |
| **Erlang** | [`helloworld.erl`](languages/erlang/hello-world/helloworld.erl) | ✅ |  |
| **F#** | [`HelloWorld.fs`](languages/f-sharp/hello-world/HelloWorld.fs) | ✅ |  |
| **GAMS** | [`HelloWorld.gms`](languages/gams/hello-world/HelloWorld.gms) |  |  |
| **Groovy** | [`HelloWorld.groovy`](languages/groovy/hello-world/HelloWorld.groovy) | ✅ |  |
| **Io** | [`HelloWorld.io`](languages/io/hello-world/HelloWorld.io) | ✅ |  |
| **J** | [`HelloWorld.ijs`](languages/j/hello-world/HelloWorld.ijs) | ✅ |  |
| **J#** | [`HelloWorld.jsl`](languages/j-sharp/hello-world/HelloWorld.jsl) |  |  |
| **JScript** | [`HelloWorld.js`](languages/jscript/hello-world/HelloWorld.js) | ✅ | Windows Script Host |
| **Logo** | [`HelloWorld.logo`](languages/logo/hello-world/HelloWorld.logo) | ✅ |  |
| **ML** | [`HelloWorld.sml`](languages/standard-ml/hello-world/HelloWorld.sml) | ✅ |  |
| **MS-DOS batch** | [`HelloWorld.bat`](languages/batch/hello-world/HelloWorld.bat) | ✅ |  |
| **NetLogo** | [`HelloWorld.nls`](languages/netlogo/hello-world/HelloWorld.nls) |  |  |
| **Nim** | [`HelloWorld.nim`](languages/nim/hello-world/HelloWorld.nim) | ✅ |  |
| **OpenCL** | [`HelloWorld.cl`](languages/opencl/hello-world/HelloWorld.cl) | 🔧 |  |
| **PL/I** | [`HelloWorld.pli`](languages/pl-i/hello-world/HelloWorld.pli) | ✅ |  |
| **PowerScript** | [`HelloWorld.powerscript`](languages/powerscript/hello-world/HelloWorld.powerscript) |  |  |
| **Pure Data** | [`HelloWorld.pd`](languages/pure-data/hello-world/HelloWorld.pd) | ✅ | patch file; prints to the Pd console |
| **PureBasic** | [`HelloWorld.pb`](languages/purebasic/hello-world/HelloWorld.pb) |  |  |
| **Q** | [`HelloWorld.q`](languages/q/hello-world/HelloWorld.q) |  |  |
| **REBOL** | [`HelloWorld.reb`](languages/rebol/hello-world/HelloWorld.reb) | ✅ |  |
| **Ring** | [`HelloWorld.ring`](languages/ring/hello-world/HelloWorld.ring) | ✅ |  |
| **Scheme** | [`HelloWorld.scm`](languages/scheme/hello-world/HelloWorld.scm) | ✅ |  |
| **Solidity** | [`HelloWorld.sol`](languages/solidity/hello-world/HelloWorld.sol) | 🔧 |  |
| **Structured Text** | [`HelloWorld.st`](languages/structured-text/hello-world/HelloWorld.st) | 🔧 | IEC 61131-3 |
| **Tcl** | [`HelloWorld.tcl`](languages/tcl/hello-world/HelloWorld.tcl) | ✅ |  |
| **tcsh** | [`HelloWorld.tcsh`](languages/tcsh/hello-world/HelloWorld.tcsh) | ✅ |  |
| **thinBasic** | [`HelloWorld.tbasic`](languages/thinbasic/hello-world/HelloWorld.tbasic) |  |  |
| **V** | [`HelloWorld.v`](languages/v/hello-world/HelloWorld.v) |  |  |
| **Xbase++** | [`HelloWorld.prg`](languages/xbase-plus-plus/hello-world/HelloWorld.prg) | ✅ |  |
| **XC** | [`HelloWorld.xc`](languages/xc/hello-world/HelloWorld.xc) | ✅ |  |
| **Xojo** | [`HelloWorld.xojo_code`](languages/xojo/hello-world/HelloWorld.xojo_code) |  |  |
| **XPL** | [`HelloWorld.xpl`](languages/xpl/hello-world/HelloWorld.xpl) |  |  |
| **Z shell** | [`HelloWorld.zsh`](languages/z-shell/hello-world/HelloWorld.zsh) | ✅ |  |

## Historical languages

Languages that shaped programming, ordered by the year they first appeared.

| Language | Year | File | CI | Notes |
|---|---|---|---|---|
| **MAD** | 1959 | [`HELLO.mad`](languages/mad/hello-world/HELLO.mad) |  | Michigan Algorithm Decoder |
| **RPG** | 1959 | [`HelloWorld.rpgle`](languages/rpg/hello-world/HelloWorld.rpgle) |  | modern free-form RPG IV |
| **ALGOL 60** | 1960 | [`HelloWorld.alg`](languages/algol-60/hello-world/HelloWorld.alg) | ✅ |  |
| **JOSS** | 1963 | [`HelloWorld.joss`](languages/joss/hello-world/HelloWorld.joss) |  |  |
| **BASIC** | 1964 | [`HelloWorld.bas`](languages/basic/hello-world/HelloWorld.bas) | ✅ |  |
| **JCL** | 1964 | [`HELLO.jcl`](languages/jcl/hello-world/HELLO.jcl) |  | IBM mainframe Job Control Language |
| **ALGOL W** | 1966 | [`HelloWorld.alw`](languages/algol-w/hello-world/HelloWorld.alw) | ✅ |  |
| **APL** | 1966 | [`HelloWorld.apl`](languages/apl/hello-world/HelloWorld.apl) | ✅ |  |
| **MUMPS (M)** | 1966 | [`HelloWorld.m`](languages/mumps/hello-world/HelloWorld.m) | ✅ |  |
| **Simula** | 1967 | [`HelloWorld.sim`](languages/simula/hello-world/HelloWorld.sim) | ✅ |  |
| **SNOBOL4** | 1967 | [`HelloWorld.sno`](languages/snobol4/hello-world/HelloWorld.sno) | ✅ |  |
| **ALGOL 68** | 1968 | [`HelloWorld.a68`](languages/algol-68/hello-world/HelloWorld.a68) | ✅ |  |
| **FOCAL** | 1968 | [`HelloWorld.foc`](languages/focal/hello-world/HelloWorld.foc) | ✅ |  |
| **B** | 1969 | [`HelloWorld.b`](languages/b/hello-world/HelloWorld.b) | ✅ |  |
| **Forth** | 1970 | [`HelloWorld.fth`](languages/forth/hello-world/HelloWorld.fth) | ✅ |  |
| **Pascal** | 1970 | [`HelloWorld.pas`](languages/pascal/hello-world/HelloWorld.pas) | ✅ |  |
| **INTERCAL** | 1972 | [`HelloWorld.i`](languages/intercal/hello-world/HelloWorld.i) | ✅ |  |
| **Smalltalk** | 1972 | [`HelloWorld.st`](languages/smalltalk/hello-world/HelloWorld.st) | ✅ |  |
| **COMAL** | 1973 | [`HelloWorld.lst`](languages/comal/hello-world/HelloWorld.lst) | ✅ |  |
| **Ratfor** | 1974 | [`HelloWorld.r`](languages/ratfor/hello-world/HelloWorld.r) | ✅ |  |
| **CLU** | 1975 | [`HelloWorld.clu`](languages/clu/hello-world/HelloWorld.clu) |  |  |
| **Commodore BASIC** | 1977 | [`HelloWorld.bas`](languages/commodore-basic/hello-world/HelloWorld.bas) | ✅ |  |
| **Icon** | 1977 | [`HelloWorld.icn`](languages/icon/hello-world/HelloWorld.icn) | ✅ |  |
| **Hope** | 1978 | [`HelloWorld.hop`](languages/hope/hello-world/HelloWorld.hop) | ✅ |  |
| **Modula-2** | 1978 | [`HelloWorld.mod`](languages/modula-2/hello-world/HelloWorld.mod) | ✅ |  |
| **dBase** | 1979 | [`HelloWorld.prg`](languages/dbase/hello-world/HelloWorld.prg) | ✅ |  |
| **REXX** | 1979 | [`HelloWorld.rexx`](languages/rexx/hello-world/HelloWorld.rexx) | ✅ |  |
| **BBC BASIC** | 1981 | [`HelloWorld.bbc`](languages/bbc-basic/hello-world/HelloWorld.bbc) | ✅ |  |
| **PostScript** | 1982 | [`HelloWorld.ps`](languages/postscript/hello-world/HelloWorld.ps) | ✅ |  |
| **Turing** | 1982 | [`HelloWorld.t`](languages/turing/hello-world/HelloWorld.t) |  |  |
| **occam** | 1983 | [`HelloWorld.occ`](languages/occam/hello-world/HelloWorld.occ) |  |  |
| **Standard ML** | 1983 | [`HelloWorld.sml`](languages/standard-ml/hello-world/HelloWorld.sml) | ✅ |  |
| **Verilog / SystemVerilog** | 1984 | [`HelloWorld.sv`](languages/verilog/hello-world/HelloWorld.sv) | ✅ |  |
| **Clipper** | 1985 | [`HelloWorld.prg`](languages/clipper/hello-world/HelloWorld.prg) | ✅ |  |
| **Miranda** | 1985 | [`HelloWorld.mira`](languages/miranda/hello-world/HelloWorld.mira) | ✅ |  |
| **Eiffel** | 1986 | [`hello_world.e`](languages/eiffel/hello-world/hello_world.e) | ✅ |  |
| **ABC** | 1987 | [`HelloWorld.abc`](languages/abc/hello-world/HelloWorld.abc) | ✅ |  |
| **HyperTalk** | 1987 | [`HelloWorld.hypertalk`](languages/hypertalk/hello-world/HelloWorld.hypertalk) |  |  |
| **Oberon** | 1987 | [`HelloWorld.Mod`](languages/oberon/hello-world/HelloWorld.Mod) | ✅ |  |
| **Self** | 1987 | [`HelloWorld.self`](languages/self/hello-world/HelloWorld.self) |  |  |
| **Lingo** | 1988 | [`HelloWorld.ls`](languages/lingo/hello-world/HelloWorld.ls) |  |  |
| **Modula-3** | 1988 | [`Main.m3`](languages/modula-3/hello-world/Main.m3) | ✅ |  |
| **Sather** | 1990 | [`HelloWorld.sa`](languages/sather/hello-world/HelloWorld.sa) |  |  |
| **TI-BASIC** | 1990 | [`HELLO.8xp.txt`](languages/ti-basic/hello-world/HELLO.8xp.txt) |  | TI-83/84 calculators |
| **QBasic** | 1991 | [`HELLO.BAS`](languages/qbasic/hello-world/HELLO.BAS) | ✅ |  |
| **NewtonScript** | 1993 | [`HelloWorld.nwt`](languages/newtonscript/hello-world/HelloWorld.nwt) | ✅ |  |
| **Limbo** | 1995 | [`HelloWorld.b`](languages/limbo/hello-world/HelloWorld.b) |  |  |
| **LotusScript** | 1995 | [`HelloWorld.lss`](languages/lotusscript/hello-world/HelloWorld.lss) |  |  |
| **Python 2** | 2000 | [`HelloWorld.py`](languages/python-2/hello-world/HelloWorld.py) | ✅ |  |

## Modern & trending languages

New or fast-growing languages that are not (yet) in the TIOBE top 100.

| Language | File | CI | Notes |
|---|---|---|---|
| **Ballerina** | [`HelloWorld.bal`](languages/ballerina/hello-world/HelloWorld.bal) | ✅ |  |
| **Bend** | [`HelloWorld.bend`](languages/bend/hello-world/HelloWorld.bend) | ✅ |  |
| **C3** | [`HelloWorld.c3`](languages/c3/hello-world/HelloWorld.c3) | ✅ |  |
| **Carbon** | [`HelloWorld.carbon`](languages/carbon/hello-world/HelloWorld.carbon) | ✅ | experimental |
| **Chapel** | [`HelloWorld.chpl`](languages/chapel/hello-world/HelloWorld.chpl) | ✅ |  |
| **Crystal** | [`HelloWorld.cr`](languages/crystal/hello-world/HelloWorld.cr) | ✅ |  |
| **Elm** | [`Main.elm`](languages/elm/hello-world/Main.elm) | 🔧 |  |
| **Gleam** | [`HelloWorld.gleam`](languages/gleam/hello-world/HelloWorld.gleam) | ✅ |  |
| **Grain** | [`HelloWorld.gr`](languages/grain/hello-world/HelloWorld.gr) | ✅ |  |
| **Hare** | [`HelloWorld.ha`](languages/hare/hello-world/HelloWorld.ha) | ✅ |  |
| **Haxe** | [`HelloWorld.hx`](languages/haxe/hello-world/HelloWorld.hx) | ✅ |  |
| **Inko** | [`HelloWorld.inko`](languages/inko/hello-world/HelloWorld.inko) | ✅ |  |
| **Jai** | [`HelloWorld.jai`](languages/jai/hello-world/HelloWorld.jai) |  | closed beta |
| **Koka** | [`helloworld.kk`](languages/koka/hello-world/helloworld.kk) | ✅ |  |
| **Lean 4** | [`HelloWorld.lean`](languages/lean/hello-world/HelloWorld.lean) | ✅ |  |
| **Mojo** | [`HelloWorld.mojo`](languages/mojo/hello-world/HelloWorld.mojo) | ✅ |  |
| **MoonBit** | [`HelloWorld.mbt`](languages/moonbit/hello-world/HelloWorld.mbt) | ✅ |  |
| **Odin** | [`HelloWorld.odin`](languages/odin/hello-world/HelloWorld.odin) | ✅ |  |
| **Pony** | [`HelloWorld.pony`](languages/pony/hello-world/HelloWorld.pony) | ✅ |  |
| **Q#** | [`HelloWorld.qs`](languages/q-sharp/hello-world/HelloWorld.qs) | ✅ |  |
| **Racket** | [`HelloWorld.rkt`](languages/racket/hello-world/HelloWorld.rkt) | ✅ |  |
| **Raku (Perl 6)** | [`HelloWorld.raku`](languages/raku/hello-world/HelloWorld.raku) | ✅ |  |
| **ReScript** | [`HelloWorld.res`](languages/rescript/hello-world/HelloWorld.res) | ✅ |  |
| **Roc** | [`HelloWorld.roc`](languages/roc/hello-world/HelloWorld.roc) | ✅ |  |
| **Unison** | [`HelloWorld.u`](languages/unison/hello-world/HelloWorld.u) | ✅ |  |
| **Vala** | [`HelloWorld.vala`](languages/vala/hello-world/HelloWorld.vala) | ✅ |  |
| **WebAssembly (WAT)** | [`HelloWorld.wat`](languages/webassembly/hello-world/HelloWorld.wat) | ✅ |  |

## More general-purpose languages

Functional, logic, object-oriented and scripting languages outside the TIOBE top 100.

| Language | File | CI | Notes |
|---|---|---|---|
| **Agda** | [`HelloWorld.agda`](languages/agda/hello-world/HelloWorld.agda) | ✅ |  |
| **Alice ML** | [`HelloWorld.aml`](languages/alice-ml/hello-world/HelloWorld.aml) |  |  |
| **Arc** | [`HelloWorld.arc`](languages/arc/hello-world/HelloWorld.arc) | ✅ |  |
| **AssemblyScript** | [`HelloWorld.ts`](languages/assemblyscript/hello-world/HelloWorld.ts) | ✅ |  |
| **ATS** | [`HelloWorld.dats`](languages/ats/hello-world/HelloWorld.dats) | ✅ |  |
| **Austral** | [`HelloWorld.aum`](languages/austral/hello-world/HelloWorld.aum) | ✅ |  |
| **AutoLISP** | [`HelloWorld.lsp`](languages/autolisp/hello-world/HelloWorld.lsp) |  |  |
| **Babashka** | [`HelloWorld.bb`](languages/babashka/hello-world/HelloWorld.bb) | ✅ |  |
| **Beef** | [`Program.bf`](languages/beef/hello-world/Program.bf) |  |  |
| **Berry** | [`HelloWorld.be`](languages/berry/hello-world/HelloWorld.be) | ✅ |  |
| **Boo** | [`HelloWorld.boo`](languages/boo/hello-world/HelloWorld.boo) | ✅ |  |
| **Carp** | [`HelloWorld.carp`](languages/carp/hello-world/HelloWorld.carp) | ✅ |  |
| **Ceylon** | [`run.ceylon`](languages/ceylon/hello-world/run.ceylon) | ✅ |  |
| **CHICKEN Scheme** | [`HelloWorld.scm`](languages/chicken-scheme/hello-world/HelloWorld.scm) | ✅ |  |
| **Civet** | [`HelloWorld.civet`](languages/civet/hello-world/HelloWorld.civet) | ✅ |  |
| **Clean** | [`HelloWorld.icl`](languages/clean/hello-world/HelloWorld.icl) | ✅ |  |
| **ClojureScript** | [`HelloWorld.cljs`](languages/clojurescript/hello-world/HelloWorld.cljs) | ✅ |  |
| **Cobra** | [`HelloWorld.cobra`](languages/cobra/hello-world/HelloWorld.cobra) | ✅ |  |
| **COOL** | [`HelloWorld.cl`](languages/cool/hello-world/HelloWorld.cl) |  | Classroom Object Oriented Language; two variants |
| **Cpp2 (cppfront)** | [`HelloWorld.cpp2`](languages/cppfront/hello-world/HelloWorld.cpp2) | ✅ |  |
| **Curry** | [`HelloWorld.curry`](languages/curry/hello-world/HelloWorld.curry) | ✅ |  |
| **Cyclone** | [`HelloWorld.cyc`](languages/cyclone/hello-world/HelloWorld.cyc) |  |  |
| **Dafny** | [`HelloWorld.dfy`](languages/dafny/hello-world/HelloWorld.dfy) | ✅ |  |
| **Dylan** | [`hello-world.dylan`](languages/dylan/hello-world/hello-world.dylan) | ✅ |  |
| **Emacs Lisp** | [`HelloWorld.el`](languages/emacs-lisp/hello-world/HelloWorld.el) | ✅ |  |
| **Eta** | [`Main.hs`](languages/eta/hello-world/Main.hs) | ✅ |  |
| **Euphoria** | [`HelloWorld.ex`](languages/euphoria/hello-world/HelloWorld.ex) | ✅ |  |
| **F*** | [`HelloWorld.fst`](languages/fstar/hello-world/HelloWorld.fst) | 🔧 |  |
| **Factor** | [`hello-world.factor`](languages/factor/hello-world/hello-world.factor) | ✅ |  |
| **Fantom** | [`HelloWorld.fan`](languages/fantom/hello-world/HelloWorld.fan) | ✅ |  |
| **Fennel** | [`HelloWorld.fnl`](languages/fennel/hello-world/HelloWorld.fnl) | ✅ |  |
| **FreeBASIC** | [`HelloWorld.bas`](languages/freebasic/hello-world/HelloWorld.bas) | ✅ |  |
| **Frege** | [`HelloWorld.fr`](languages/frege/hello-world/HelloWorld.fr) | ✅ |  |
| **G-Portugol** | [`HelloWorld.gpt`](languages/g-portugol/hello-world/HelloWorld.gpt) | ✅ | open source Portugol compiler, 2005 |
| **Genie** | [`HelloWorld.gs`](languages/genie/hello-world/HelloWorld.gs) | ✅ |  |
| **Golo** | [`HelloWorld.golo`](languages/golo/hello-world/HelloWorld.golo) | ✅ |  |
| **Gosu** | [`HelloWorld.gsp`](languages/gosu/hello-world/HelloWorld.gsp) | ✅ |  |
| **Hack** | [`HelloWorld.hack`](languages/hack/hello-world/HelloWorld.hack) | ✅ |  |
| **HolyC** | [`HelloWorld.HC`](languages/holyc/hello-world/HelloWorld.HC) | ✅ |  |
| **Hy** | [`HelloWorld.hy`](languages/hy/hello-world/HelloWorld.hy) | ✅ |  |
| **Hylo** | [`HelloWorld.hylo`](languages/hylo/hello-world/HelloWorld.hylo) | ✅ |  |
| **Idris** | [`HelloWorld.idr`](languages/idris/hello-world/HelloWorld.idr) | ✅ |  |
| **Imba** | [`HelloWorld.imba`](languages/imba/hello-world/HelloWorld.imba) | ✅ |  |
| **Jakt** | [`HelloWorld.jakt`](languages/jakt/hello-world/HelloWorld.jakt) |  |  |
| **Janet** | [`HelloWorld.janet`](languages/janet/hello-world/HelloWorld.janet) | ✅ |  |
| **Joy** | [`HelloWorld.joy`](languages/joy/hello-world/HelloWorld.joy) | ✅ |  |
| **Juliar** | [`HelloWorld.jrl`](languages/juliar/hello-world/HelloWorld.jrl) |  |  |
| **Kotlin Script** | [`HelloWorld.main.kts`](languages/kotlin-script/hello-world/HelloWorld.main.kts) | ✅ |  |
| **LFE** | [`HelloWorld.lfe`](languages/lfe/hello-world/HelloWorld.lfe) | ✅ |  |
| **LiveScript** | [`HelloWorld.ls`](languages/livescript/hello-world/HelloWorld.ls) | ✅ |  |
| **Lobster** | [`HelloWorld.lobster`](languages/lobster/hello-world/HelloWorld.lobster) | ✅ |  |
| **Logtalk** | [`hello_world.lgt`](languages/logtalk/hello-world/hello_world.lgt) | ✅ |  |
| **Mercury** | [`helloworld.m`](languages/mercury/hello-world/helloworld.m) | ✅ |  |
| **MoonScript** | [`HelloWorld.moon`](languages/moonscript/hello-world/HelloWorld.moon) | ✅ |  |
| **Nelua** | [`HelloWorld.nelua`](languages/nelua/hello-world/HelloWorld.nelua) | ✅ |  |
| **Nemerle** | [`HelloWorld.n`](languages/nemerle/hello-world/HelloWorld.n) |  |  |
| **NetRexx** | [`HelloWorld.nrx`](languages/netrexx/hello-world/HelloWorld.nrx) | ✅ |  |
| **newLISP** | [`HelloWorld.lsp`](languages/newlisp/hello-world/HelloWorld.lsp) | ✅ |  |
| **Objective-J** | [`HelloWorld.j`](languages/objective-j/hello-world/HelloWorld.j) | ✅ |  |
| **Oxygene** | [`HelloWorld.pas`](languages/oxygene/hello-world/HelloWorld.pas) |  |  |
| **Oz** | [`HelloWorld.oz`](languages/oz/hello-world/HelloWorld.oz) | ✅ |  |
| **Pawn** | [`HelloWorld.pwn`](languages/pawn/hello-world/HelloWorld.pwn) | ✅ |  |
| **Picat** | [`hello_world.pi`](languages/picat/hello-world/hello_world.pi) | ✅ |  |
| **PicoLisp** | [`HelloWorld.l`](languages/picolisp/hello-world/HelloWorld.l) | ✅ |  |
| **Pike** | [`HelloWorld.pike`](languages/pike/hello-world/HelloWorld.pike) | ✅ |  |
| **Portugol (VisuAlg)** | [`HelloWorld.alg`](languages/visualg/hello-world/HelloWorld.alg) | ✅ | pseudocode used to teach programming in Brazil |
| **Portugol Studio** | [`HelloWorld.por`](languages/portugol-studio/hello-world/HelloWorld.por) | ✅ | UNIVALI |
| **Potigol** | [`HelloWorld.poti`](languages/potigol/hello-world/HelloWorld.poti) | ✅ | IFRN, functional language in Portuguese |
| **Processing** | [`HelloWorld.pde`](languages/processing/hello-world/HelloWorld.pde) | ✅ |  |
| **PureScript** | [`Main.purs`](languages/purescript/hello-world/Main.purs) | ✅ |  |
| **ReasonML** | [`HelloWorld.re`](languages/reasonml/hello-world/HelloWorld.re) | ✅ |  |
| **Red** | [`HelloWorld.red`](languages/red/hello-world/HelloWorld.red) | ✅ |  |
| **Rocq (Coq)** | [`HelloWorld.v`](languages/coq/hello-world/HelloWorld.v) | ✅ |  |
| **Seed7** | [`HelloWorld.sd7`](languages/seed7/hello-world/HelloWorld.sd7) | ✅ |  |
| **Shen** | [`HelloWorld.shen`](languages/shen/hello-world/HelloWorld.shen) | ✅ |  |
| **Small Basic** | [`HelloWorld.sb`](languages/small-basic/hello-world/HelloWorld.sb) |  |  |
| **Terra** | [`HelloWorld.t`](languages/terra/hello-world/HelloWorld.t) | ✅ |  |
| **Toit** | [`hello.toit`](languages/toit/hello-world/hello.toit) | ✅ |  |
| **Umka** | [`HelloWorld.um`](languages/umka/hello-world/HelloWorld.um) | ✅ |  |
| **Unicon** | [`HelloWorld.icn`](languages/unicon/hello-world/HelloWorld.icn) | ✅ |  |
| **Vale** | [`HelloWorld.vale`](languages/vale/hello-world/HelloWorld.vale) | ✅ |  |
| **Wren** | [`HelloWorld.wren`](languages/wren/hello-world/HelloWorld.wren) | ✅ |  |
| **X10** | [`HelloWorld.x10`](languages/x10/hello-world/HelloWorld.x10) | ✅ |  |
| **Xtend** | [`HelloWorld.xtend`](languages/xtend/hello-world/HelloWorld.xtend) | ✅ |  |
| **Zephir** | [`World.zep`](languages/zephir/hello-world/World.zep) | ✅ |  |
| **Égua / Delégua** | [`HelloWorld.egua`](languages/egua/hello-world/HelloWorld.egua) | ✅ | Delégua is a fork of Égua and runs `.egua` files |

## Assembly, IR & bytecode

Machine-level languages for specific architectures and virtual machines.

| Language | File | CI | Notes |
|---|---|---|---|
| **Assembly (6502, Commodore 64)** | [`HelloWorld.asm`](languages/assembly-6502/hello-world/HelloWorld.asm) | 🔧 | 64tass syntax; `SYS 49152` to run |
| **Assembly (ARM64, Linux)** | [`HelloWorld.s`](languages/assembly-arm64-linux/hello-world/HelloWorld.s) | ✅ |  |
| **Assembly (ARM64, macOS)** | [`HelloWorld.s`](languages/assembly-arm64-macos/hello-world/HelloWorld.s) | ✅ |  |
| **Assembly (MIPS, SPIM/MARS)** | [`HelloWorld.asm`](languages/assembly-mips/hello-world/HelloWorld.asm) | ✅ |  |
| **Assembly (RISC-V, Linux)** | [`HelloWorld.s`](languages/assembly-risc-v/hello-world/HelloWorld.s) | ✅ |  |
| **Assembly (x86-64, Linux, NASM)** | [`HelloWorld.asm`](languages/assembly-x86-64-linux/hello-world/HelloWorld.asm) | ✅ |  |
| **Assembly (Z80, CP/M)** | [`HELLO.ASM`](languages/assembly-z80/hello-world/HELLO.ASM) | ✅ |  |
| **C--** | [`HelloWorld.cmm`](languages/c-minus-minus/hello-world/HelloWorld.cmm) |  |  |
| **CIL (.NET IL)** | [`HelloWorld.il`](languages/cil/hello-world/HelloWorld.il) | ✅ |  |
| **JVM bytecode (Jasmin)** | [`HelloWorld.j`](languages/jasmin/hello-world/HelloWorld.j) | ✅ |  |
| **LLVM IR** | [`HelloWorld.ll`](languages/llvm-ir/hello-world/HelloWorld.ll) | ✅ |  |
| **MMIX** | [`HelloWorld.mms`](languages/mmix/hello-world/HelloWorld.mms) | ✅ | Donald Knuth's architecture from *The Art of Computer Programming* |

## Shells & automation

Command shells, OS scripting and desktop automation.

| Language | File | CI | Notes |
|---|---|---|---|
| **AutoHotkey** | [`HelloWorld.ahk`](languages/autohotkey/hello-world/HelloWorld.ahk) |  |  |
| **AutoIt** | [`HelloWorld.au3`](languages/autoit/hello-world/HelloWorld.au3) |  |  |
| **Dash** | [`HelloWorld.sh`](languages/dash/hello-world/HelloWorld.sh) | ✅ |  |
| **dc** | [`HelloWorld.dc`](languages/dc/hello-world/HelloWorld.dc) | ✅ |  |
| **Elvish** | [`HelloWorld.elv`](languages/elvish/hello-world/HelloWorld.elv) | ✅ |  |
| **Expect** | [`HelloWorld.exp`](languages/expect/hello-world/HelloWorld.exp) | ✅ |  |
| **fish** | [`HelloWorld.fish`](languages/fish/hello-world/HelloWorld.fish) | ✅ |  |
| **Google Apps Script** | [`Code.gs`](languages/google-apps-script/hello-world/Code.gs) |  |  |
| **JavaScript for Automation (JXA)** | [`HelloWorld.js`](languages/jxa/hello-world/HelloWorld.js) | ✅ |  |
| **jq** | [`HelloWorld.jq`](languages/jq/hello-world/HelloWorld.jq) | ✅ |  |
| **KiXtart** | [`HelloWorld.kix`](languages/kixtart/hello-world/HelloWorld.kix) |  |  |
| **Korn shell** | [`HelloWorld.ksh`](languages/korn-shell/hello-world/HelloWorld.ksh) | ✅ |  |
| **LibreOffice Basic** | [`HelloWorld.bas`](languages/libreoffice-basic/hello-world/HelloWorld.bas) |  |  |
| **m4** | [`HelloWorld.m4`](languages/m4/hello-world/HelloWorld.m4) | ✅ |  |
| **mIRC scripting** | [`HelloWorld.mrc`](languages/mirc-script/hello-world/HelloWorld.mrc) |  |  |
| **Nushell** | [`HelloWorld.nu`](languages/nushell/hello-world/HelloWorld.nu) | ✅ |  |
| **rc (Plan 9 shell)** | [`HelloWorld.rc`](languages/rc/hello-world/HelloWorld.rc) | ✅ |  |
| **sed** | [`HelloWorld.sed`](languages/sed/hello-world/HelloWorld.sed) | ✅ |  |
| **VBA** | [`HelloWorld.bas`](languages/vba/hello-world/HelloWorld.bas) |  | Microsoft Office macros |
| **Vim script** | [`HelloWorld.vim`](languages/vim-script/hello-world/HelloWorld.vim) | ✅ |  |
| **Windows CMD (NT batch)** | [`HelloWorld.cmd`](languages/cmd/hello-world/HelloWorld.cmd) | ✅ |  |
| **Xonsh** | [`HelloWorld.xsh`](languages/xonsh/hello-world/HelloWorld.xsh) | ✅ |  |
| **YSH (Oils)** | [`HelloWorld.ysh`](languages/ysh/hello-world/HelloWorld.ysh) | ✅ |  |

## Scientific, math & statistics

Numerical computing, computer algebra and statistics.

| Language | File | CI | Notes |
|---|---|---|---|
| **AMPL** | [`HelloWorld.run`](languages/ampl/hello-world/HelloWorld.run) | ✅ |  |
| **BQN** | [`HelloWorld.bqn`](languages/bqn/hello-world/HelloWorld.bqn) | ✅ |  |
| **GAP** | [`HelloWorld.g`](languages/gap/hello-world/HelloWorld.g) | ✅ |  |
| **GAUSS** | [`HelloWorld.gss`](languages/gauss/hello-world/HelloWorld.gss) |  |  |
| **GNU Octave** | [`HelloWorld.m`](languages/gnu-octave/hello-world/HelloWorld.m) | ✅ |  |
| **gnuplot** | [`HelloWorld.gp`](languages/gnuplot/hello-world/HelloWorld.gp) | ✅ |  |
| **IDL** | [`HelloWorld.pro`](languages/idl/hello-world/HelloWorld.pro) | ✅ |  |
| **K** | [`HelloWorld.k`](languages/k/hello-world/HelloWorld.k) | ✅ |  |
| **Macaulay2** | [`HelloWorld.m2`](languages/macaulay2/hello-world/HelloWorld.m2) | ✅ |  |
| **Magma** | [`HelloWorld.m`](languages/magma/hello-world/HelloWorld.m) |  |  |
| **Maple** | [`HelloWorld.mpl`](languages/maple/hello-world/HelloWorld.mpl) |  |  |
| **Maxima** | [`HelloWorld.mac`](languages/maxima/hello-world/HelloWorld.mac) | ✅ |  |
| **MiniZinc** | [`HelloWorld.mzn`](languages/minizinc/hello-world/HelloWorld.mzn) | ✅ |  |
| **Modelica** | [`HelloWorld.mo`](languages/modelica/hello-world/HelloWorld.mo) | ✅ |  |
| **Nial** | [`HelloWorld.ndf`](languages/nial/hello-world/HelloWorld.ndf) | ✅ |  |
| **PARI/GP** | [`HelloWorld.gp`](languages/pari-gp/hello-world/HelloWorld.gp) | ✅ |  |
| **REDUCE** | [`HelloWorld.red`](languages/reduce/hello-world/HelloWorld.red) | ✅ |  |
| **SageMath** | [`HelloWorld.sage`](languages/sagemath/hello-world/HelloWorld.sage) | ✅ |  |
| **Scilab** | [`HelloWorld.sce`](languages/scilab/hello-world/HelloWorld.sce) | ✅ |  |
| **SPSS Syntax** | [`HelloWorld.sps`](languages/spss/hello-world/HelloWorld.sps) | ✅ |  |
| **Stan** | [`HelloWorld.stan`](languages/stan/hello-world/HelloWorld.stan) | ✅ |  |
| **Stata** | [`HelloWorld.do`](languages/stata/hello-world/HelloWorld.do) |  |  |
| **Uiua** | [`HelloWorld.ua`](languages/uiua/hello-world/HelloWorld.ua) | ✅ |  |
| **Wolfram Language (Mathematica)** | [`HelloWorld.wl`](languages/wolfram/hello-world/HelloWorld.wl) | ✅ |  |

## Query languages

Databases, graphs and data querying.

| Language | File | CI | Notes |
|---|---|---|---|
| **Cypher** | [`HelloWorld.cypher`](languages/cypher/hello-world/HelloWorld.cypher) | ✅ |  |
| **Datalog (Soufflé)** | [`HelloWorld.dl`](languages/souffle/hello-world/HelloWorld.dl) | ✅ |  |
| **DAX** | [`HelloWorld.dax`](languages/dax/hello-world/HelloWorld.dax) |  |  |
| **Excel formula** | [`HelloWorld.xlsx.txt`](languages/excel/hello-world/HelloWorld.xlsx.txt) | ✅ | type it into any cell |
| **GraphQL** | [`HelloWorld.graphql`](languages/graphql/hello-world/HelloWorld.graphql) | 🔧 | schema plus query; the resolver returns "Hello World" |
| **KQL (Kusto)** | [`HelloWorld.kql`](languages/kql/hello-world/HelloWorld.kql) |  |  |
| **Natural** | [`HELLO.nsp`](languages/natural/hello-world/HELLO.nsp) |  |  |
| **OpenEdge ABL (Progress 4GL)** | [`HelloWorld.p`](languages/openedge-abl/hello-world/HelloWorld.p) |  |  |
| **PL/pgSQL** | [`HelloWorld.sql`](languages/pl-pgsql/hello-world/HelloWorld.sql) | ✅ |  |
| **Power Query M** | [`HelloWorld.pq`](languages/power-query-m/hello-world/HelloWorld.pq) |  |  |
| **SPARQL** | [`HelloWorld.rq`](languages/sparql/hello-world/HelloWorld.rq) | ✅ |  |
| **Splunk SPL** | [`HelloWorld.spl`](languages/splunk-spl/hello-world/HelloWorld.spl) |  |  |
| **SQLite SQL** | [`HelloWorld.sql`](languages/sqlite/hello-world/HelloWorld.sql) | ✅ |  |
| **XQuery** | [`HelloWorld.xq`](languages/xquery/hello-world/HelloWorld.xq) | ✅ |  |

## Hardware, GPU & quantum

Hardware description, GPU kernels and quantum programs.

| Language | File | CI | Notes |
|---|---|---|---|
| **Amaranth HDL** | [`hello_world.py`](languages/amaranth/hello-world/hello_world.py) | ✅ |  |
| **Bluespec SystemVerilog** | [`HelloWorld.bsv`](languages/bluespec/hello-world/HelloWorld.bsv) | ✅ |  |
| **Chisel** | [`HelloWorld.scala`](languages/chisel/hello-world/HelloWorld.scala) | 🔧 |  |
| **CUDA** | [`HelloWorld.cu`](languages/cuda/hello-world/HelloWorld.cu) | 🔧 |  |
| **GLSL** | [`HelloWorld.comp`](languages/glsl/hello-world/HelloWorld.comp) | 🔧 | Vulkan compute shader with `debugPrintfEXT` |
| **HLSL** | [`HelloWorld.hlsl`](languages/hlsl/hello-world/HelloWorld.hlsl) | 🔧 |  |
| **Metal Shading Language** | [`HelloWorld.metal`](languages/metal/hello-world/HelloWorld.metal) |  |  |
| **OpenQASM** | [`HelloWorld.qasm`](languages/openqasm/hello-world/HelloWorld.qasm) | 🔧 | quantum circuit; no text output |
| **SystemC** | [`HelloWorld.cpp`](languages/systemc/hello-world/HelloWorld.cpp) | ✅ |  |
| **WGSL** | [`HelloWorld.wgsl`](languages/wgsl/hello-world/HelloWorld.wgsl) | 🔧 | no text output; renders a solid color |

## Smart contracts

Blockchain and smart-contract languages.

| Language | File | CI | Notes |
|---|---|---|---|
| **Cairo** | [`hello_world.cairo`](languages/cairo/hello-world/hello_world.cairo) | ✅ |  |
| **Clarity** | [`hello-world.clar`](languages/clarity/hello-world/hello-world.clar) | 🔧 |  |
| **ink! (Rust)** | [`lib.rs`](languages/ink/hello-world/lib.rs) | 🔧 |  |
| **Michelson (Tezos)** | [`hello_world.tz`](languages/michelson/hello-world/hello_world.tz) | ✅ |  |
| **Move** | [`hello_world.move`](languages/move/hello-world/hello_world.move) | 🔧 |  |
| **Sway (Fuel)** | [`main.sw`](languages/sway/hello-world/main.sw) | 🔧 |  |
| **Vyper** | [`HelloWorld.vy`](languages/vyper/hello-world/HelloWorld.vy) | 🔧 |  |
| **Yul** | [`HelloWorld.yul`](languages/yul/hello-world/HelloWorld.yul) | 🔧 |  |

## Game & embedded scripting

Languages embedded in game engines and applications.

| Language | File | CI | Notes |
|---|---|---|---|
| **AGS Script (Adventure Game Studio)** | [`GlobalScript.asc`](languages/ags-script/hello-world/GlobalScript.asc) |  |  |
| **AngelScript** | [`HelloWorld.as`](languages/angelscript/hello-world/HelloWorld.as) | ✅ |  |
| **Arduino** | [`HelloWorld.ino`](languages/arduino/hello-world/HelloWorld.ino) | 🔧 |  |
| **BlitzBasic** | [`HelloWorld.bb`](languages/blitzbasic/hello-world/HelloWorld.bb) |  |  |
| **ChaiScript** | [`HelloWorld.chai`](languages/chaiscript/hello-world/HelloWorld.chai) | ✅ |  |
| **GDScript (Godot)** | [`hello_world.gd`](languages/gdscript/hello-world/hello_world.gd) | ✅ |  |
| **Gravity** | [`HelloWorld.gravity`](languages/gravity/hello-world/HelloWorld.gravity) | ✅ |  |
| **Inform 7** | [`story.ni`](languages/inform-7/hello-world/story.ni) | ✅ |  |
| **LSL (Second Life)** | [`HelloWorld.lsl`](languages/lsl/hello-world/HelloWorld.lsl) | 🔧 |  |
| **Luau (Roblox)** | [`HelloWorld.luau`](languages/luau/hello-world/HelloWorld.luau) | ✅ |  |
| **MicroPython** | [`main.py`](languages/micropython/hello-world/main.py) | ✅ |  |
| **Minecraft function** | [`hello.mcfunction`](languages/mcfunction/hello-world/hello.mcfunction) | 🔧 |  |
| **Papyrus (Skyrim)** | [`HelloWorld.psc`](languages/papyrus/hello-world/HelloWorld.psc) |  |  |
| **PICO-8 Lua** | [`hello.p8.lua`](languages/pico-8/hello-world/hello.p8.lua) |  |  |
| **QuakeC** | [`progs.qc`](languages/quakec/hello-world/progs.qc) | 🔧 |  |
| **Ren'Py** | [`script.rpy`](languages/renpy/hello-world/script.rpy) | 🔧 |  |
| **Squirrel** | [`HelloWorld.nut`](languages/squirrel/hello-world/HelloWorld.nut) | ✅ |  |
| **Teal** | [`HelloWorld.tl`](languages/teal/hello-world/HelloWorld.tl) | ✅ |  |
| **UnrealScript** | [`HelloWorld.uc`](languages/unrealscript/hello-world/HelloWorld.uc) |  |  |
| **YueScript** | [`HelloWorld.yue`](languages/yuescript/hello-world/HelloWorld.yue) | ✅ |  |
| **ZIL (Zork Implementation Language)** | [`hello.zil`](languages/zil/hello-world/hello.zil) | ✅ |  |

## Markup, templates & web

Documents, stylesheets and templates. They render or produce "Hello World" instead of printing it.

| Language | File | CI | Notes |
|---|---|---|---|
| **AsciiDoc** | [`HelloWorld.adoc`](languages/asciidoc/hello-world/HelloWorld.adoc) | ✅ |  |
| **Astro** | [`HelloWorld.astro`](languages/astro/hello-world/HelloWorld.astro) | ✅ |  |
| **Blade (Laravel)** | [`hello.blade.php`](languages/blade/hello-world/hello.blade.php) | ✅ |  |
| **Classic ASP** | [`HelloWorld.asp`](languages/asp-classic/hello-world/HelloWorld.asp) |  |  |
| **CSS** | [`HelloWorld.css`](languages/css/hello-world/HelloWorld.css) | 🔧 |  |
| **EJS** | [`HelloWorld.ejs`](languages/ejs/hello-world/HelloWorld.ejs) | ✅ |  |
| **Encapsulated PostScript** | [`HelloWorld.eps`](languages/postscript-eps/hello-world/HelloWorld.eps) | ✅ |  |
| **ERB (Embedded Ruby)** | [`HelloWorld.erb`](languages/erb/hello-world/HelloWorld.erb) | ✅ |  |
| **Graphviz DOT** | [`HelloWorld.dot`](languages/graphviz-dot/hello-world/HelloWorld.dot) | 🔧 |  |
| **Haml** | [`HelloWorld.haml`](languages/haml/hello-world/HelloWorld.haml) | ✅ |  |
| **Handlebars** | [`HelloWorld.hbs`](languages/handlebars/hello-world/HelloWorld.hbs) | 🔧 |  |
| **HTML** | [`HelloWorld.html`](languages/html/hello-world/HelloWorld.html) | ✅ |  |
| **Jinja** | [`HelloWorld.jinja`](languages/jinja/hello-world/HelloWorld.jinja) | ✅ |  |
| **JSP** | [`HelloWorld.jsp`](languages/jsp/hello-world/HelloWorld.jsp) | ✅ |  |
| **JSX (React)** | [`HelloWorld.jsx`](languages/jsx/hello-world/HelloWorld.jsx) | ✅ |  |
| **LaTeX** | [`HelloWorld.tex`](languages/latex/hello-world/HelloWorld.tex) | ✅ |  |
| **Liquid** | [`HelloWorld.liquid`](languages/liquid/hello-world/HelloWorld.liquid) | ✅ |  |
| **Markdown** | [`HelloWorld.md`](languages/markdown/hello-world/HelloWorld.md) | ✅ |  |
| **MDX** | [`HelloWorld.mdx`](languages/mdx/hello-world/HelloWorld.mdx) | ✅ |  |
| **Mermaid** | [`HelloWorld.mmd`](languages/mermaid/hello-world/HelloWorld.mmd) | 🔧 |  |
| **Mustache** | [`HelloWorld.mustache`](languages/mustache/hello-world/HelloWorld.mustache) | ✅ |  |
| **Org mode** | [`HelloWorld.org`](languages/org-mode/hello-world/HelloWorld.org) | ✅ |  |
| **PlantUML** | [`HelloWorld.puml`](languages/plantuml/hello-world/HelloWorld.puml) | ✅ |  |
| **Pug** | [`HelloWorld.pug`](languages/pug/hello-world/HelloWorld.pug) | ✅ |  |
| **Razor (ASP.NET)** | [`HelloWorld.cshtml`](languages/razor/hello-world/HelloWorld.cshtml) | ✅ |  |
| **reStructuredText** | [`HelloWorld.rst`](languages/restructuredtext/hello-world/HelloWorld.rst) | ✅ |  |
| **RTF** | [`HelloWorld.rtf`](languages/rtf/hello-world/HelloWorld.rtf) | ✅ |  |
| **Slim** | [`HelloWorld.slim`](languages/slim/hello-world/HelloWorld.slim) | ✅ |  |
| **Svelte** | [`HelloWorld.svelte`](languages/svelte/hello-world/HelloWorld.svelte) | ✅ |  |
| **SVG** | [`HelloWorld.svg`](languages/svg/hello-world/HelloWorld.svg) | ✅ |  |
| **TeX (plain)** | [`HelloWorld.tex`](languages/tex/hello-world/HelloWorld.tex) | ✅ |  |
| **troff / groff** | [`HelloWorld.ms`](languages/troff/hello-world/HelloWorld.ms) | ✅ |  |
| **Twig** | [`HelloWorld.twig`](languages/twig/hello-world/HelloWorld.twig) | ✅ |  |
| **Typst** | [`HelloWorld.typ`](languages/typst/hello-world/HelloWorld.typ) | ✅ |  |
| **VRML** | [`HelloWorld.wrl`](languages/vrml/hello-world/HelloWorld.wrl) | 🔧 |  |
| **Vue (SFC)** | [`HelloWorld.vue`](languages/vue/hello-world/HelloWorld.vue) | ✅ |  |
| **XML** | [`HelloWorld.xml`](languages/xml/hello-world/HelloWorld.xml) | ✅ |  |

## Configuration, build & infrastructure

Build systems, configuration languages and infrastructure as code.

| Language | File | CI | Notes |
|---|---|---|---|
| **Ansible** | [`hello-world.yml`](languages/ansible/hello-world/hello-world.yml) | ✅ |  |
| **Apache Ant** | [`build.xml`](languages/ant/hello-world/build.xml) | ✅ |  |
| **Bicep** | [`main.bicep`](languages/bicep/hello-world/main.bicep) | 🔧 |  |
| **CMake** | [`HelloWorld.cmake`](languages/cmake/hello-world/HelloWorld.cmake) | ✅ |  |
| **CUE** | [`HelloWorld.cue`](languages/cue/hello-world/HelloWorld.cue) | ✅ |  |
| **Dhall** | [`HelloWorld.dhall`](languages/dhall/hello-world/HelloWorld.dhall) | ✅ |  |
| **Dockerfile** | [`Dockerfile`](languages/dockerfile/hello-world/Dockerfile) | ✅ |  |
| **GitHub Actions** | [`hello-world.yml`](languages/github-actions/hello-world/hello-world.yml) | 🔧 |  |
| **Gradle Kotlin DSL** | [`build.gradle.kts`](languages/gradle-kotlin-dsl/hello-world/build.gradle.kts) | ✅ |  |
| **HCL (Terraform)** | [`main.tf`](languages/hcl/hello-world/main.tf) | ✅ |  |
| **JSON** | [`hello.json`](languages/json/hello-world/hello.json) | ✅ |  |
| **Jsonnet** | [`HelloWorld.jsonnet`](languages/jsonnet/hello-world/HelloWorld.jsonnet) | ✅ |  |
| **just** | [`justfile`](languages/just/hello-world/justfile) | ✅ |  |
| **KCL** | [`HelloWorld.k`](languages/kcl/hello-world/HelloWorld.k) | ✅ |  |
| **Make** | [`Makefile`](languages/make/hello-world/Makefile) | ✅ |  |
| **Meson** | [`meson.build`](languages/meson/hello-world/meson.build) | ✅ |  |
| **Nickel** | [`HelloWorld.ncl`](languages/nickel/hello-world/HelloWorld.ncl) | ✅ |  |
| **Nix** | [`HelloWorld.nix`](languages/nix/hello-world/HelloWorld.nix) | ✅ |  |
| **Pkl** | [`HelloWorld.pkl`](languages/pkl/hello-world/HelloWorld.pkl) | ✅ |  |
| **Puppet** | [`hello_world.pp`](languages/puppet/hello-world/hello_world.pp) | ✅ |  |
| **Rego (Open Policy Agent)** | [`hello.rego`](languages/rego/hello-world/hello.rego) | ✅ |  |
| **Starlark (Bazel)** | [`BUILD.bazel`](languages/bazel-starlark/hello-world/BUILD.bazel) | ✅ |  |
| **TOML** | [`hello.toml`](languages/toml/hello-world/hello.toml) | ✅ |  |
| **YAML** | [`hello.yaml`](languages/yaml/hello-world/hello.yaml) | ✅ |  |

## Brazilian languages 🇧🇷

Languages created in Brazil or designed for programming in Portuguese. Some of them also appear in other tables.

| Language | File | CI | Notes |
|---|---|---|---|
| **BIRL** | [`HelloWorld.birl`](languages/birl/hello-world/HelloWorld.birl) | ✅ | keywords from bodybuilder Bambam's catchphrases |
| **Elixir** | [`HelloWorld.exs`](languages/elixir/hello-world/HelloWorld.exs) | ✅ | created by José Valim, 2012 |
| **G-Portugol** | [`HelloWorld.gpt`](languages/g-portugol/hello-world/HelloWorld.gpt) | ✅ | open source Portugol compiler, 2005 |
| **Lua** | [`HelloWorld.lua`](languages/lua/hello-world/HelloWorld.lua) | ✅ | PUC-Rio, 1993 — the most widely used Brazilian language |
| **Portugol (VisuAlg)** | [`HelloWorld.alg`](languages/visualg/hello-world/HelloWorld.alg) | ✅ | pseudocode used to teach programming in Brazil |
| **Portugol Studio** | [`HelloWorld.por`](languages/portugol-studio/hello-world/HelloWorld.por) | ✅ | UNIVALI |
| **Potigol** | [`HelloWorld.poti`](languages/potigol/hello-world/HelloWorld.poti) | ✅ | IFRN, functional language in Portuguese |
| **Égua / Delégua** | [`HelloWorld.egua`](languages/egua/hello-world/HelloWorld.egua) | ✅ | Delégua is a fork of Égua and runs `.egua` files |

## Esoteric languages

Languages designed as jokes, puzzles or experiments.

| Language | File | CI | Notes |
|---|---|---|---|
| **ArnoldC** | [`HelloWorld.arnoldc`](languages/arnoldc/hello-world/HelloWorld.arnoldc) | ✅ |  |
| **Befunge** | [`HelloWorld.bf93`](languages/befunge/hello-world/HelloWorld.bf93) | ✅ |  |
| **BIRL** | [`HelloWorld.birl`](languages/birl/hello-world/HelloWorld.birl) | ✅ | keywords from bodybuilder Bambam's catchphrases |
| **Brainfuck** | [`HelloWorld.bf`](languages/brainfuck/hello-world/HelloWorld.bf) | ✅ |  |
| **Chef** | [`HelloWorld.chef`](languages/chef/hello-world/HelloWorld.chef) | ✅ |  |
| **COW** | [`HelloWorld.cow`](languages/cow/hello-world/HelloWorld.cow) | ✅ | generated from the Brainfuck program |
| **Emojicode** | [`HelloWorld.emojic`](languages/emojicode/hello-world/HelloWorld.emojic) | ✅ |  |
| **FALSE** | [`HelloWorld.f`](languages/false/hello-world/HelloWorld.f) |  |  |
| **GolfScript** | [`HelloWorld.gs`](languages/golfscript/hello-world/HelloWorld.gs) | ✅ |  |
| **HQ9+** | [`HelloWorld.hq9`](languages/hq9-plus/hello-world/HelloWorld.hq9) | ✅ | `H` prints "Hello, world!" |
| **LOLCODE** | [`HelloWorld.lol`](languages/lolcode/hello-world/HelloWorld.lol) | ✅ |  |
| **Ook!** | [`HelloWorld.ook`](languages/ook/hello-world/HelloWorld.ook) | ✅ | generated from the Brainfuck program |
| **Piet** | [`HelloWorld.txt`](languages/piet/hello-world/HelloWorld.txt) |  | image-based; link to the canonical program |
| **Pyth** | [`HelloWorld.pyth`](languages/pyth/hello-world/HelloWorld.pyth) | ✅ |  |
| **Rockstar** | [`HelloWorld.rock`](languages/rockstar/hello-world/HelloWorld.rock) | ✅ |  |
| **Shakespeare** | [`HelloWorld.spl`](languages/shakespeare/hello-world/HelloWorld.spl) | ✅ |  |
| **Unlambda** | [`HelloWorld.unl`](languages/unlambda/hello-world/HelloWorld.unl) | ✅ |  |
| **Whitespace** | [`HelloWorld.ws`](languages/whitespace/hello-world/HelloWorld.ws) | ✅ |  |

## Running the tests

```sh
python3 scripts/hello.py check              # metadata, files and README are consistent
python3 scripts/hello.py test               # run every language whose toolchain is installed locally
python3 scripts/hello.py test --lang python --lang rust
python3 scripts/hello.py test --changed-since origin/master   # only languages changed on this branch
python3 scripts/hello.py readme             # regenerate this README from languages/*/language.json and */meta.json
```

## Contributing

The catalog is organized **by language, with one folder per algorithm inside it**:

```
languages/<lang>/
├── language.json          # the language: name, section or TIOBE position, year, notes
├── hello-world/           # the startup-cost baseline every language has
│   ├── meta.json          # files and test of this implementation
│   └── HelloWorld.<ext>
└── <algorithm>/           # more classic algorithms (see docs/specs/010-algorithm-set)
```

1. Check the tables above: is the language already covered?
2. For a new language, create `languages/<lang>/` (lowercase, hyphens) with a `language.json`:
   ```json
   {"name": "Python", "section": "general", "notes": ""}
   ```
   `section` is one of: `historical`, `modern`, `general`, `assembly`, `shells`, `scientific`, `query`, `hardware`, `blockchain`, `game`, `markup`, `config`, `esoteric`.
3. Add the implementation in `languages/<lang>/<algorithm>/` (`hello-world` first) with the program and a `meta.json`:
   ```json
   {"files": ["HelloWorld.py"], "test": {"group": "base", "run": "python3 HelloWorld.py"}}
   ```
   `test` is optional: add it when the language can run on a GitHub runner. `group` is `base` (tools preinstalled
   on Ubuntu), `apt` (with an `"apt": ["package"]` list), `extra` (tools set up in the workflow), `macos` or
   `windows`, or `docker` (with a pinned `"image"`; `run` executes inside it). `needs` lists the commands that must
   exist (defaults to the first word of `run`). Set `"kind": "compile"` when the program cannot print and the test
   only checks that the official tool accepts it.
4. The program should be the idiomatic, minimal version for that language; Hello World prints (or displays) `Hello World`.
5. Run `python3 scripts/hello.py readme` and `python3 scripts/hello.py check`, then open a pull request.

## Contributors

Maintained by [@matbrgz](https://github.com/matbrgz).

[![matbrgz](https://github.com/matbrgz.png?size=64)](https://github.com/matbrgz)

[![Contributors](https://contrib.rocks/image?repo=BenchCommons/catalog-algorithms)](https://github.com/BenchCommons/catalog-algorithms/graphs/contributors)

## License

[MIT](LICENSE)
