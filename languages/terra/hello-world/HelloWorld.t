local C = terralib.includec("stdio.h")

terra hello()
  C.printf("Hello World\n")
end

hello()
