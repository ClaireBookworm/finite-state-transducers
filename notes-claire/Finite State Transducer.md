- compact rep & lexical rules, or idioms and cliches 
- FSM is motivated by considerations of time and space efficiency
	- time efficiency is usually achieved using deterministic automata
	- space efficiency is achieved with classical minimiztion algorithm for deterministic automata
- applications to NLP

## String-to-string transducers
- seq transducers: determine input
- output of sequency transitions isn't deterministic

## Types of Machines

In the theory of computation, a Moore machine is a finite-state machine whose current output values are determined only by its current state. This is in contrast to a Mealy machine, whose output values are determined both by its current state and by the values of its inputs. 

https://hackage.haskell.org/package/machines-0.4.1/docs/Data-Machine-Mealy.html
https://hackage.haskell.org/package/machines-0.4.1/docs/Data-Machine-Moore.html 

**MOORE**
- 6 tuple: Q, q0, alphabet, output alphabet, transition function delta, and output function 
- state diagram moore diagram -> diagram state diagram that associates an output value iwth each state 

PROCESS 
https://hackage.haskell.org/package/machines-0.4.1/docs/Data-Machine-Process.html#t:Process
A Process `a b` is a stream transducer that can consume values of type `a` from its input, and produce values of type `b` for its output.

A ProcessT m a b is a stream transducer that can consume values of type a from its input, and produce values of type b and has side-effects in the Monad m.

```haskell
type Process a b = Machine (Is a) b
type ProcessT m a b = MachineT m (Is a) b
```

So far, there's a pattern in the 3 machines (mealy, moore, fst) -- all recursively refers to itself for "what to do next"; replace that with any type `next`

`newtype MealyF a b next = MealyF { runMealyF :: a -> (b, next) }`

By using a base functor we get rid of recursion. -> the base function is called STEP 
https://hackage.haskell.org/package/machines-0.4.1/docs/Data-Machine-Type.html#t:Step 

