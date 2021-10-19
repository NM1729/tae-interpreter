# tae-interpreter
An interpreter for the language of typed arithmetic expressions.

The interpreter has been developed in Python language.

## Language of Arithmetic Expressions

The language of arithmetic expressions is an extension to the language of booleans, containing additional terms and evaluation rules.

### Terms

* true
* false
* 0
* if t1 then t2 else t3
* succ t1
* pred t1
* iszero t1

### Values

* true
* false
* nv

nv denotes numerical values, which are either:

* 0
* succ nv

Eg: 0, succ 0, succ succ 0

### Evaluation rules

Language of arithmetic expressions contain evaluation rules from the language of booleans as well as its own.

1. E-IFTRUE

if true then t2 else t3 -> t2

2. E-IFFALSE

if false then t2 else t3 -> t3

3. E-IF

t1 -> t1' / if t1 then t2 else t3 -> if t1' then t2 else t3

The rule before the / denotes a precondition.

4. E-ISZEROZERO

iszero 0 -> true

5. E-ISZEROSUCC

iszero succ nv -> false

6. E-ISZERO

t1->t1' / iszero t1 -> iszero t1'

7. E-PREDZERO

pred 0 -> 0

8. E-PREDSUCC

pred succ nv1 -> nv1

9. E-PRED

t1 -> t1' / pred t1 -> pred t1'

10. E-SUCC

t1 -> t1' / succ t1 -> succ t1'

### Properties of Language of Arithmetic Expressions

1. **Every Normal Form is not a value**
2. **Determinacy of one-step evaluation**- 

If t->t' and t->t", then t'=t"

3. **Uniqueness of Normal Forms**-

If t-*->u and t-*->u', then u=u'

-*-> denotes complete evaluation.

4. **Termination of evaluation**

Every evaluation of a term terminates.

### Abstract Syntax Tree

An Abstract Syntax Tree(AST) is a tree-like representation of the structure of code.

Eg: AST for if (iszero succ 0) then pred 0 else false

```
        if-then-else
|           |           |
iszero      pred        false
|           |
succ        0
|
0
```


