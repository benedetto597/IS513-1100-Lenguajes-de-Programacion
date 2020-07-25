with Ada.Text_IO, Ada.Integer_Text_IO, Ada.Long_Long_Integer_Text_IO;

procedure Factorial is
begin
   declare 
      function Fact (N: Integer) return Long_Long_Integer is
      begin
         if N=0 then
            return 1;
         else 
            return Long_Long_Integer(N)*Fact(N-1);
         end if;
      end Fact;
   i: Integer := 0;
   begin
      loop
         Ada.Integer_Text_IO.Put (Item => i, Width => 1);
         Ada.Text_IO.Put ("! = ");
         Ada.Long_Long_Integer_Text_IO.Put (Item => Fact(i), Width => 1);
         Ada.Text_IO.New_Line;
         i := i + 1;
         exit when i=17;
      end loop;
   end;
end Factorial;
