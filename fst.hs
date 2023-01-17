-- fST HASKELL


-- mealy -> reads an `a` from a stream of inputs `a` and outputs a `b` to a stream of outputs; reads first and then outputs once after reading

newtype Mealy a b = Mealy { runMealy :: a -> (b, Mealy a b) }

-- moore -> outputs a `b` to a stream of outputs and reads an input `a` from a stream of inputs; starts with output of b and then reads once after each output

data Moore a b = Moore b (a -> Moore a b) 

-- fst either reads from its input, writes to its outputs, or stops 
-- can read as many times in a row as it wants & write as many times in a row as it wants

data FST a b
    = Read  (a -> FST a b)
    | Write (b,   FST a b)
    | Stop

-- PROCESS

newtype MealyF a b next = MealyF { runMealyF :: a -> (b, next) }
-- the moore machine, after outputting and requesting an input, figures out the next machine to run 

data MooreF a b next = MooreF b (a -> next)

data FSTF a b next
    = Read  (a -> next)
    | Write (b,   next)
    | Stop
-- ^^ when we write to the output we'll also provide what to do next after outputting; when we stop, there's nothing next

-- this eliminiates explicit RECURSION

data Step k o r
  = forall t. Await (t -> r) (k t) r
  | Yield o r
  | Stop
-- step has renamed the type varialbe for the output to `o`, what to do next to `r`, reading to `Awaird`, and writing to `Yield`