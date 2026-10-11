entity HelloWorld is
end entity HelloWorld;

architecture sim of HelloWorld is
begin
    process
    begin
        report "Hello World";
        wait;
    end process;
end architecture sim;
