https://docs.jock.org/

Introduction to Jock
Jock is a subject-oriented statically-typed functional programming language which compiles to Nock and can run on any Nock VM (currently Zorp's Sword and Urbit's Vere runtimes). It inherits many conventions from Urbit's Hoon language, and its reference parser and compiler are written in Hoon.

Jock is developed by Zorp Corp and is currently in pre-alpha development.

Here are some short programs in Jock:

Copy
// Demonstrate a conditional statement.

let a: @ = 3;

if a == 3 {
  72
} else if a == 5 {
  17
} else {
  15
}
Copy
// Create a decrement function, the long way around.

let dec = (a:@  -> @) {
  let b = 0;
  loop;
  if a == +(b) {
    b
  } else {
    b = +(b);
    recur
  }
};

dec(5)
Copy
// Demonstrate a loop.

let a: @ = 5;
let b: @ = 0;
loop;
if a == +(b) {
  b
} else {
  b = +(b);
  $
}


Keywords
Jock currently supports the following keywords:

let: variable and function assignment

if: boolean decision

else: boolean decision, other branch

crash: end program

assert: positive assertion

object: core with named arms

compose: compose subjects

loop: loop start point, similar to do/|-

defer: unexecuted closure (trap/quote)

recur: loop recursion point, similar to continue

match: switch over type/Hoon ?+/?- or case/C switch, with _ as default case

eval: evaluate raw Nock

with: indicates predicate for compose

this: ., the current subject

Compiler
The purpose of a compiler is to transform source code as text into executable code on a particular instruction set architecture (ISA). Jock is a high-level language which is compiled using Hoon to run directly on the Nock ISA.

The top-level entry points to the Jock compiler are:

++jeam, which converts a cord text input to a jock AST.

++mint:cj, which converts a jock AST input to [nock jype].

There is also a ++mint entry point which contains the entire cord→[nock jype] build chain in a single function.

Internally, Jock code is built in several stages. The compiler first tokenizes the input, then builds the AST, and finally compiles the AST into Nock.

++parse-tokens tokenizes the input, yielding a (list token).

Copy
let a = {
  eval [42 55] [0 2]
};

a
→

Copy
~[[%keyword %let] [%name %a] [%punctuator %'='] [%punctuator %'{'] [%keyword %eval] [%punctuator %'['] [%literal [%number 42]] [%literal [%number 55]] [%punctuator %']'] [%punctuator %'['] [%literal [%number 0]] [%literal [%number 2]] [%punctuator %']'] [%punctuator %'}'] [%punctuator %';'] [%name %a]]
++match-jock converts a (list token) to a jock.

Copy
[%let type=[p=[%untyped ~] name=%a] val=[%eval p=[p=[%atom p=[%number 42]] q=[%atom p=[%number 55]]] q=[p=[%atom p=[%number 0]] q=[%atom p=[%number 2]]]] next=[%limb p=~[[%name p=%a]]]]
++mint:cj converts a jock to a nock.

Copy
[8 [2 [[1 42] 1 55] [1 0] 1 2] 0 2]
Tokenizer
A $token may be one of a keyword, a punctuator, a literal, or a name.

Copy
+$  token
  $+  token
  $%  [%keyword keyword]
      [%punctuator punctuator]
      [%symbol jatom]
      [%literal jatom]
      [%name term]
  ==
%keyword denotes one of the registered keywords in +$keyword. Keywords serve for control flow.

%punctuator denotes one of the registered punctuators in +$punctuator. Punctuators include clause prefix/suffix pairs; compound operators like -> are built of subsequent tokens. A number of punctuators are special-cased later on in the AST builder, such a + Nock increment operator. These serve for data syntax and control flow.

%symbol denotes a constant jatom.

%literal denotes a regular jatom.

%name denotes a limb lookup label. Names are arbitrary terms.

Literals and symbols may be one of:

%number, a Hoon-style @ud unsigned decimal.

%hexadecimal, a Hoon-style @ux unsigned hexadecimal.

%loobean, a Hoon-style ? loobean.

%string, a single-quoted Hoon-style @t cord.

(The symbol/literal distinction is currently necessary for type checking on atoms in match cases.)

Jock currently recognizes spaces and newlines as constituting whitespace. Comments are C-style, and may begin with a // and end with a newline or be delimited by /* and */.

AST Builder
AST
The target of the AST builder is to produce a jock AST.

A jock is a type union over the kinds of expressions which Jock knows about. Some of these derive directly from keywords and literals, while others are syntactically parsed from special-case punctuation. A jock is either a cell of jocks or a head-tagged value containing the relevant expression (frequently a keyword of a limb or value invocation).

For instance, the operation of +(a) increments the value of a, ultimately using a Nock 4. Here, it is parsed into the following jock:

Copy
[%increment [%limb ~[[%name %a]]]]
Ultimately, this will yield a Nock expression something like the following:

Copy
[%4 %0 16]
with an appropriate axis lookup for the name a (here represented as 16).

To understand jock, we need to consider the following basic set of AST expressions:

%atom

%limb

%edit

%call

Some of these expressions include a next=jock component, which indicates that they alter the subject for a set of daughter jocks.

%atom

Copy
[%atom p=jatom]
A Nock atom (a fortiori, a Hoon atom) is an integer of arbitrary size. An atom may have an associated type (derived from its literal form) which denotes it as a number, a string, etc. (Jock does not currently support arbitrary Hoon atom types; it is limited to the following. Eventually, this list will be expanded in a principled way.)

Copy
+$  jatom
  $+  jatom
  $~  [%loobean %.n]
  $%  [%string term]
      [%number @ud]
      [%hexadecimal @ux]
      [%loobean ?]
  ==
The following are examples of %atoms.

false → [%atom %loobean %.n]

5 → [%atom %number 5]

'hello' → [%atom %string %hello] = [%atom %string `term`478.560.413.032]

0x4f → [%atom %hexadecimal 0x4f] = [%atom %hexadecimal `@ux`79]

(Strings are likely too restrictive as terms. Number should probably be collapsed somewhat into a single type. Currently I have added a %symbol to propagate constants, but this may be unnecessary if we put a constant flag in there instead.)

%limb

Copy
[%limb p=(list jlimb)]
A limb is a lookup label for a particular axis in the subject. Typically, the end developer will never need to know the actual axis, since the limb serves as the index in the higher-level language. A limb may resolve either as a leg (Nock 0 axis lookup) or an arm (Nock 9 axis lookup); this matters in the compilation stage but not earlier.

Copy
+$  jlimb
  $%  [%name p=term]
      [%axis p=@]
  ==
The following are examples of %limbs.

add → [%limb ~[%name %add]]

a → [%limb ~[%name %a]]

&2 → [%limb ~[[%axis p=2]]

. → [%limb ~[[%axis 1]]]

%edit

Copy
[%edit limb=(list jlimb) val=jock next=jock]
An %edit indicates a change to the value associated with a %limb. For instance, this would take place with assignment, either in a let clause or a subsequent reassignment.

b = 5; → [%edit limb=~[[%name p=%b]] val=[%atom %number 5]]]

b = +(b); → [%edit limb=~[[%name p=%b]] val=[%increment val=[%limb p=~[[%name p=%b]]]] next=*jock]

%call

Copy
[%call func=jock arg=(unit jock)]
A %call is a function invocation. More concretely, it is the invocation of a jock with an optional argument. Typically, this jock will be either a %limb, an %axis, or a %lambda expression.

One strange place you see %call occur: as the next clause in a jock that shouldn't be reachable (like %else). In this case, [%call func=[%limb p=~[[%axis p=0]]] arg=~] will reduce to an (uncalled) [0 0] crash.

Functions and Cores
A %core is simply either a single lambda function (a gate) or a map of names to types. As actually constructed, the (map term jype) is a correlation of faces to %jlimbs; while names or axes, these ultimately resolve in either legs (raw data, Nock 0) or arms ($lambda-argument, Nock 9).

Copy
+$  core-body  (each lambda-argument (map term jype))
::
+$  jlimb
  $%  [%name p=term]
      [%axis p=@]
  ==
::
+$  lambda
  $+  lambda
  [arg=lambda-argument body=jock payload=(unit jock)]
::
+$  lambda-argument
  $+  lambda-argument
  [inp=(unit jype) out=jype]
At this point, Jock distinguishes two kinds of function invocations: a gate (%lambda) or a more general core (%limb or %axis).

A %lambda invocation results in simply a straightforward gate call at %$. Since Jock actually specifies the input and output types from a function, the jype or Jock type is included in the +$lambda-argument.

The Lifecycle of a Program
Trivial Atom

Consider the short and trivial program,

Copy
42
This program begins its lifecycle as plaintext. The cord is supplied to ++parse-tokens, which yields the symbols,

Copy
~[[%literal [[%number 42] %.n]]]
indicating that it is a non-constant decimal literal with the value 42.

This +$token is consumed in ++jeam, which utilizes ++match-jock to recursively produce a +$jock. In this case, the incoming literal is passed to ++match-literal, where it is converted directly into,

Copy
[%atom [[%number 42] %.n]]
Since no other tokens follow, ++match-jock returns the +$jock.

The +$jock is consumed by ++mint:cj. We supply the |cj door a generic subject +$jype [[%atom %string %.n] %$]. The top element of the +$jock, in this case, is an [%atom p=jatom], so this is directly converted to a single Nock 1 and a corresponding +$jype.

Copy
:-  [%1 42]
[[%atom [%number %.n]] %$]
Assignment and Return

Consider the program,

Copy
let a:@ = 42;

a
As before, the plaintext cord is supplied to ++parse-tokens to obtain the symbols,

Copy
~[[%keyword %let] [%name %a] [%punctuator %':'] [%punctuator %'@'] [%punctuator %'='] [%literal [[%number 42] %.n]] [%punctuator %';'] [%name %a]]
This list of +$tokens is passed to ++jeam. Each token is considered, and likely indicates the consumption of several following tokens. At the highest level, the entire program is structured as a single %let with its dependent clauses for type, val, and next.

type is produced using ++match-jype which consumes the name and the optional type annotation;

= is consumed as a required punctuator;

val is produced using ++match-inner-jock

; is consumed as a required terminator;

next is produced as the “rest of the owl”, that is, the successor clauses in the program.

++jeam
: 
type

The Jock expression a:@ resolves into a name with an associated type of atom. This is strictly a type, since no value is explicit here. Type can be a cell, in which case the +$jype is recursively built, but in this case it is merely a non-constant atom @.

Copy
[[%atom p=%number q=%.n] %a]
++jeam
: 
val

The value is parsed much as the raw atom from the previous program.

Copy
[%atom [[%number 42] %.n]]
++jeam
: 
next

In this case, the remainder of the program which nests under this subject consists of a simple limb. The name must be registered as a limb, which must be looked up in the next step.

Copy
[%limb p=~[[%name p=%a]]]
After the +$jock expression for the program has been assembled, it looks like this:

Copy
:*  %let
    type=[[%atom p=%number q=%.n] %a]
    val=[%atom [[%number 42] %.n]]
    next=[%limb ~[[%name %a]]]
==
The ++minting of this program is in parts trivial (the atom reduces to a Nock 1) and in parts more complex (converted the limb lookup to an axis).

++mint
: 
type
/
val

In the first place, a typecheck is performed, wherein the type and the val are compared to make sure that the value nests in the declared type. This is done by producing the pair of +$nock and +$jype for val, then using the |jt core to “unify” the type, or see if the jypes of type and val-jyp nest properly.

The jypes are:

type: [[%atom p=%number q=%.n] %a]

val-jyp: [[%atom p=%number q=%.n] %$]

++unify:jt recursively checks the jypes to see if they nest properly. As of this version of Jock, this consists simply of a structural check, check for %none, and then an assertion that the declared types match. (I.e., %decimal and %hexadecimal would not nest.)

The subject is then modified using Nock 8 to push the variable.

++mint
: 
next

The remainder of the program consists of a limb lookup. This takes place in two parts: first a wing (limb search path) is generated, then resolved against the appropriate subject.

A ++get-limb search takes place in |jt against the current jype. If a %name is being sought, then a search through the tree of the current jype is carried out until the name is matched and the corresponding wing is returned.

The incoming jype, in this case, is the current jype associated with the %let; thus the name %a is already registered.

~[[%name %a]]

The single entry of %name is looked up using ++axis-at-name, which recursively searches in the jype tree until the relative axis of the correct match is found. This value is then handed off to ++resolve-wing:jt for conversion to an appropriate Nock 0 (leg) or Nock 9 (arm).

The final result of ++mint:cj is to push a literal atom onto the subject with Nock 8 and then invoke it as a leg by axis with Nock 0. A commitment to return an unnamed atom is made in the associated jype.

Copy
:-  [8 [1 42] 0 2]
[[%atom %number %.n] %$]
Untyped 
%let

A closely related program elides the type declaration on a, requiring the type to be inferred.

Copy
let a = 42;

a
In that case, type=[[%none ~] %a]. The major difference occurs when the typecheck in ++mint:cj is carried out. Since ++unify passes all values against a %none, no real check is necessary and it returns successfully.

The final nock/jype pair is unaffected, as the typechecks are part of Jock and compile out in the final result.

Function Invocation

This Jock function is an inline function or lambda function. A Jock function includes an invocation type and a return type, and one or more executable arms.

Copy
let a: (@ -> @) = (b:@ -> @) {
  +(b)
};

a(23)
The tokenization of this program:

Copy
:~  [%keyword %let]
    [%name %a]  [%punctuator %':']
      [%punctuator %'(']
        [%punctuator %'@']
        [%punctuator %'-']  [%punctuator %'>']
        [%punctuator %'@']
      [%punctuator %')']
      [%punctuator %'=']
      [%punctuator %'(']
        [%name %b]  [%punctuator %':']  [%punctuator %'@']
        [%punctuator %'-']  [%punctuator %'>']
        [%punctuator %'@']
      [%punctuator %')']  [%punctuator %'{']
        [%punctuator %'+']  [%punctuator %'(']  [%name %b]  [%punctuator %')'
      [%punctuator %'}']  [%punctuator %';']
    [%name %a]  [%punctuator %'(']
      [%literal [[%number 23] %.n]]
    [%punctuator %')']
==
No surprises based on what we've seen before, but the multiple levels of () function declaration and invocation will require some disambiguation. (It turns out that this is the first time we are glimpsing the type declaration language, which is slightly different from vanilla “value” Jock.)

As before, %let resolves into [type val next]. We have three major differences in this program:

Function type declaration ((@->@)).

Scope-resolved/deferred variables (b).

Function invocation/gate call (a(23)).

Type Declaration

The type resolution in a conventional assignment is based on matching a name to a jype. Here we do the same thing, merely that our jype is more complex than a bare atom or cell.

++match-jype/++match-jype-leaf call into ++match-lambda-argument, which is designed to produce a +$lambda-argument. This is embedded into a core as an +$each, which is a ?-tagged type to distinguish between a regular core (object) and a lambda gate. The second element of a %core is the payload, if any. In this case, the payload is empty, indicated that the subject at the present time will be used without modification. TODO check

The resulting AST for type looks like this:

Copy
$:  :*  %core
        :*  %.y
            :*  inp=[~ [[%atom %number %.n] %$]]
                out=[[%atom %number %.n] %$]
            ==
        ==
        ~
    ==
    name=%a
==
Deferred Variables

The val serves as the body of the gate. Since we will resolve this gate by replacing its sample via Nock 9 2 10, we don't need a direct value now, only a placeholder. We simply parse the interior of the %let body as a jock.

TODO Currently, we repeat the type declaration, this time with faces. The interesting challenge, from the build perspective, will be how to collapse this into a single statement (which will require replicating information obtained at an earlier step). Not hard, but needs some attention.

Copy
:*  %lambda
    :*  arg=[inp=[~ [[%atom %number %.n] name=%b]]
             out=[[%atom %number %.n] name=%$]
            ]
        body=[%increment val=[%limb ~[[%name %b]]]]
        payload=~
    ==
==
Gate Call

The expression a(23) resolves as a +$jock %call. The func argument refers either to The arg argument is a unit delivering either no argument (as with a trap/loop) or the specified value. The tokens are built into this AST in ++match-start-name when the token '(' occurs after a %name.

Copy
:*  %call
    func=[%limb p=~[[%name %a]]]
    arg=[~ [%atom [[%number 23] %.n]]]
==
After all components have been processed, the resulting AST is:

Copy
:*  %let
    type=[[%core [%.y [inp=[~ [[%atom %number %.n] %$]] out=[[%atom %number %.n] name=%$]]] ~] name=%a]
    val=[%lambda [arg=[inp=[~ [[%atom %number %.n] name=%b]] out=[[%atom %number %.n] name=%$]] body=[%increment val=[%limb ~[[%name %b]]]] payload=~]]
    next=[%call func=[%limb ~[[%name %a]]] arg=[~ [%atom [[%number 23] %.n]]]]
==
The compilation of this AST requires ++mint:cj to handle exposing a %core in the current subject with Nock 8 and invoking it via %call with Nock 9 2 10.

As before, %let resolves its subject for type/val via ++unify:jt. First the value jype is processed as a %lambda, which is built as a Nock 8 subject injection. The output jype is merely the output value from the type declaration.

Copy
[%8
    [%1 0]        :: bunted sample
    [%1 %4 %0 6]  :: yield increment of value at sample axis
    [%0 1]        :: subject, self-return
]
This represents the sample bunt of the atom (0), the executable battery itself, and the return.

The %call in next requires the limb name and the argument, but there is of course an expectation that the associated limb be of the correct shape. Because a %lambda could be declared and called at the same time, there is a branch path to address it, but in this case we call via the %limb. The wing is resolved to an axis, and the argument itself is calculated and inserted as a Nock 1.

(Compilation to Nock from Hoon and Jock commonly results in an expression like 9 2 10 6 .... This essentially means to pull an arm from a core and edit its subject.)

The final nock reads:

Copy
[%8                     ::
    [%8                 ::
        [%1 0]          :: bunted sample
        [[%1 %4 %0 6]   :: yield increment of value at sample axis
         [%0 1]         :: subject, self-return (autocons)
        ]               ::
    ]                   ::
    [%8                               ::
        [%0 2]                        :: payload of lambda only
        [%9 2                         :: core invocation
            %10                       :: edit the default sample axis
            [6                        :: the default sample axis
                [%7 [%0 3] [%1 23]]   :: calculate and return the argument
            ]                         ::
            [%0 2]                    :: retrieve the default sample
        ]                             ::
    ]                   ::
]                       ::
Can you guess the final jype? Only an atom is returned, in the end.

Recursive Loop

Jock supports self-referential loops. (In Hoon terminology, these are called “traps”.) For instance, as Nock does not have a native decrement operator, dec is defined in terms of a recursive increment and equality check.

Copy
let dec = (a:@  -> @) {
  let b = 0;
  loop;
  if a == +(b) {
    b
  } else {
    b = +(b);
    recur
  }
};

dec(5)
The following symbols result:

Copy
~[[%keyword %let] [%name %dec] [%punctuator %'='] [%punctuator %'('] [%name %a] [%punctuator %':'] [%punctuator %'@'] [%punctuator %'-'] [%punctuator %'>'] [%punctuator %'@'] [%punctuator %')'] [%punctuator %'{'] [%keyword %let] [%name %b] [%punctuator %'='] [%literal [%number 0]] [%punctuator %';'] [%keyword %loop] [%punctuator %';'] [%keyword %if] [%name %a] [%punctuator %'='] [%punctuator %'='] [%punctuator %'+'] [%punctuator %'('] [%name %b] [%punctuator %')'] [%punctuator %'{'] [%name %b] [%punctuator %'}'] [%keyword %else] [%punctuator %'{'] [%name %b] [%punctuator %'='] [%punctuator %'+'] [%punctuator %'('] [%name %b] [%punctuator %')'] [%punctuator %';'] [%keyword %recur] [%punctuator %'}'] [%punctuator %'}'] [%punctuator %';'] [%name %dec] [%punctuator %'('] [%literal [%number 5]] [%punctuator %')']]
As with other programs starting with a let, most of the business logic is located in the next expression.

The three novel features in this program are:

The loop/recur keyword pair.

The if conditional statement. This will result in a %fork of two branches of possible logic.

The equality check. This will use Nock 5.

++jeam
: 
loop
 and 
recur

At the AST stage, a %loop refers to a single Jock daughter expression that recurs when the %recur keyword to [%call func=[%limb ~[[%axis 0]]] arg=~]. That is, having made subject modifications with an %edit or other calculation, the next clause is evaluated in that new context.

(In practice, these appear to be a syntactic GOTO, but there is a subject modification that is more explicit in the Hoon equivalent.)

The numeric axis of a limb is assessed with respect to either a name or an explicit address. The exception is [%axis 0], which looks like a crash but is in fact a shorthand indicating to locate the nearest $ arm. (Note that this means that Jock cannot currently ^ skip matches in loops.) (That resolution will take place in ++mint:cj.)

The resulting AST for this particular %loop, then, looks like this:

Copy
:*  %loop
    next=[* * *  :: various expressions, including exit case
          next=[%call func=[%limb ~[[%axis 0]]] arg=~]]]
==
++jeam
: 
if
/
else

An if statement may occur in one of two forms:

if/else

if/else if/else (iterated)

Lone C-style if statements are not supported in Jock because of how the subject is handled in Nock.

Building an AST is straightforward, resulting in a condition, a first case, and a second case.

Copy
:*  %if
    cond=[%compare a=[%limb ~[[%name %a]]] comp=%'==' b=[%increment val=[%limb ~[[%name %b]]]]]
    then=[%limb ~[[%name %b]]]
    after=[%else then=[* * *]]
==
++jeam
: 
==

A comparison requires a comparator. It is often easier to handle these (from the computer's point of view) as reverse Polish notation pushes of two values then the operand. While common in Lisps and in Hoon, this is not particularly agreeable to most developer's sense of taste, and an infix relation is preferred. To wit, contrast =(a b) and a == b. (Jock retains C-style == as an equality check.)

Copy
:*  %compare
    a=[%limb ~[[%name %a]]]
    comp=%'=='
    b=[%increment val=[%limb ~[[%name %b]]]]
==
The final Jock AST looks like this:

Copy
:*  %let
    type=[[%none ~] name=%dec]
    val=[%lambda
         [arg=[inp=[~ [[%atom %number %.n] name=%a]] out=[[%atom %number %.n] name=%$]]
          body=[%let
                type=[[%none ~] name=%b]
                val=[%atom [%number 0] %.n]
                next=[%loop
                      next=[%if
                            cond=[%compare
                                  a=[%limb ~[[%name %a]]]
                                  comp=%'=='
                                  b=[%increment val=[%limb ~[[%name %b]]]]
                                 ]
                            then=[%limb ~[[%name %b]]]
                            after=[%else then=[%edit limb=~[[%name %b]] val=[%increment val=[%limb ~[[%name %b]]]] next=[%call func=[%limb ~[[%axis 0]]] arg=~]]]
                           ]
                     ]
               ]
          payload=~
         ]
        ]
    next=[%call func=[%limb ~[[%name %dec]]] arg=[~ [%atom [%number 5] %.n]]]
==
Compiling this program has two interesting features: the %if branch conditional resolution and the %loop recursion. (The equality comparison reduces to a simple Nock 5; other kinds of comparisons will naturally be more complex.)

++mint
: 
%if

The nock for %if is straightforward: Nock 6 supports conditional branching. The jype is a %fork of a pair of the jypes of the two branches. That way, all possible return types are still accounted for correctly, even if the actual path is already fixed at compile time.

Copy
:-   [8 [8 [1 0] [1 8 [1 0] 8 [1 6 [5 [0 30] 4 0 6] [0 6] 7 [10 [6 4 0 6] 0 1] 9 2 0 1] 9 2 0 1] 0 1] 8 [0 2] 9 2 10 [6 7 [0 3] 1 5] 0 2]
[%let type=[[%none ~] name=%dec] val=[%lambda [arg=[inp=[~ [[%atom %number q=%.n] name=%a]] out=[[%atom %number q=%.n] name=%$]] body=[%let type=[[%none ~] name=%b] val=[%atom [%number 0] q=%.n] next=[%loop next=[%if cond=[%compare a=[%limb ~[[%name %a]]] comp=%'==' b=[%increment val=[%limb ~[[%name %b]]]]] then=[%limb ~[[%name %b]]] after=[%else then=[%edit limb=~[[%name %b]] val=[%increment val=[%limb ~[[%name %b]]]] next=[%call func=[%limb ~[[%axis 0]]] arg=~]]]]]] payload=~]] next=[%call func=[%limb ~[[%name %dec]]] arg=[~ [%atom [%number 5] q=%.n]]]]
++mint
: 
%loop

Since each iteration through the loop modifies the subject for the next iteration, you end up with an interesting nock of Nock 8 on 9 2 0 1, i.e. on the subject itself.

Copy
[%8                                ::
 [[%1 0]                           :: sample, default zero bunt
  [%1 %8                           :: return a constant out of the Nock 8 push
      [%1 0]                       :: counter, start from zero
      [%8                          ::
       [%1 %6                      :: if
           [%5 [%0 30] %4 [%0 6]]  ::   a == +(b)
           [%0 6]                  :: then return the sample
           [%7                     :: else
            [%10                   ::   edit the subject
             [6                    ::   at the sample axis
              [%4 [%0 6]]          ::   increment
              [%0 1]               ::   copy of subject
             ]                     ::
             [%9 %2 %0 1]]         ::   include recursion
            [%9 %2 %0 1]           ::   and actually recurse
           ]                       ::
       ]                           ::
       [%0 1]                      :: copy of the subject
      ]                            ::
  ]]                               ::
]
The result of ++mint:cj is a complex iterative calculation with a final commitment to return an unnamed atom.

Copy
:-  [%8                                 ::
     [%8                                ::
      [[%1 0]                           :: default zero bunt
       [%1 %8                           ::
           [%1 0]                       :: start from zero
           [%8                          ::
            [%1 %6                      ::
                [%5 [%0 30] %4 [%0 6]]  :: equality check on arguments
                [%0 6]                  :: if so, return the sample
                [%7                     :: else,
                 [%10                   :: edit the subject
                  [6 [%4 [%0 6]] [%0 1]] [%9 %2 %0 1]]
                 [%9 %2 %0 1]           :: and recurse
                ]                       ::
            ]                           ::
            [%0 1]                      :: copy of the subject
           ]                            ::
       ]]                               ::
      ::  dec(5)
      [%8                               ::
       [%0 2]                           :: retrieve the head (gate)
       [%9 %2 %10 6 %7 [%0 3] [%1 5]]   :: slam the gate against constant 5
      ]                                 ::
     ]                                  ::
     [%0 2]                             :: return the result (head of subject)
    ]
[[%atom %number %.n] name=%$]
Recursive Type

A container is a type which organizes other nouns. Frequently a container has type validation of some kind (e.g., contains only atoms or 2-tuples) and is capable of containing itself (as a list, set, or map).

In Jock, we enable recursive type by permitting references to existing types, including oneself. This differs from Hoon, which conceives of all types as molds, or executable gates that enforce on the type. Thus Jock must have both a type declaration system and eventually a type index for declared types.

At the time of writing, Jock's list type is manually coded into the build system. A +$jock which annotates a list is supplied:

Copy
[%list type=jype-leaf val=(list jock)]
A simple program which results in a list

Copy
let a = ~[1 2 3 4 5];

a
has a single null-terminated Hoon-style list. In this case, the type is implicitly List @, pending a proper type declaration language.

The tokenization looks like this:

Copy
~[[%keyword %let] [%name %a] [%punctuator %'='] [%punctuator %'['] [%literal [[%number 1] %.n]] [%literal [[%number 2] %.n]] [%literal [[%number 3] %.n]] [%literal [[%number 4] %.n]] [%literal [[%number 5] %.n]] [%literal [[%number 0] %.n]] [%punctuator %']'] [%punctuator %';'] [%name %a]]
To correctly handle AST generation, we need to examine what the resultant +$jype will look like. Let's consider the final compiled product first.

A naïve traversal of the list would produce this jype:

Copy
[[[[%atom %number %.n] name=%$]
   [[[[%atom %number %.n] name=%$]
    [[[[%atom %number %.n] name=%$]
     [[[[%atom %number %.n] name=%$]
      [[[[%atom %number %.n] name=%$]
        [[%atom %number %.n] name=%$]]
        name=%$]]
       name=%$]]
      name=%$]]
     name=%$]]
    name=%$]
Unfortunately, this does not preserve the “list nature” of the list. The overall jock for the list instead should be [%list [%atom jatom-type ?(%.y %.n)]]. It should build a [nock jype] pair like this:

Copy
:-  [%1 1 2 3 4 5 0]
[%list [%atom %numeric %.n]]
This convention allows even empty lists to be correctly typed at compile time, e.g.,

Copy
:-  [%1 0]
[%list [%atom %numeric %.n]]
Circling back around to the AST, ++jeam should produce this jock:

Copy
:*  %let
    type=[[%none ~] name=%a]
    val=[%list type=[%atom %number %.n] val=~[[[%atom [[%number 1] %.n]] [[%atom [[%number 2] %.n]] [[%atom [[%number 3] %.n]] [[%atom [[%number 4] %.n]] [[%atom [[%number 5] %.n]] [%atom [[%number 0] %.n]]]]]]]]]
    next=[%limb ~[[%name %a]]]
==
Thus the type is stored at a level above the null-terminated tuple. This could conceivably be supplemented by propagation of the list type information down the list, e.g.,

Copy
val=[%list type=[%atom %number %.n] val=~[[[%atom [[%number 1] %.n]] [%list type=[%atom %number %.n] val=~[[[%atom [[%number 2] %.n]] [%list type=[%atom %number %.n] val=~[[[%atom [[%number 3] %.n]] [%list type=[%atom %number %.n] val=~[[[%atom [[%number 4] %.n]] [%list type=[%atom %number %.n] val=~[[[%atom [[%number 5] %.n]] [%list type=[%atom %number %.n] val=~[[%atom [[%number 0] %.n]]]]]]]]]]]]]]]]]]]
This second option would carry the type information deeper into the type and prevent needing to pin the list context when iteratively operating on a list.

At the current time, the final compilation product of the list is the following nock:

Copy
[8 [[1 1] [1 2] [1 3] [1 4] [1 5] [1 0]] [0 2]]
Eventually there will be an optimization step in the Jock compiler at some point to yield the more sensible nock:

Copy
[%8 [%1 1 2 3 4 5 0] [%0 2]]
The Next Recursive Type

This implementation of lists requires an explicit type annotation in the +$jock. To implement sets and maps will require a similar explicit head-tagged jock entry.

Copy
[%set type=jype-leaf val=(set jock)]
[%map k=jype-leaf v=jype-leaf val=(map jype jock)]
We would like to replace this with a pure +$jype based on recursive types and references.

Copy
::  Jype types including recursion and references
+$  jype-leaf
  $%  base-jype-leaf
      ::  %ring is a recursive type with a base case
      [%ring [%atom jatom-type ?(%.y %.n)] jype]
      ::  %link is a reference to an existing type, or self if null
      [%link (unit jlimb)]
  ==
The overall jype-leaf for the list instead should be something like [%ring [%atom jatom-type ?(%.y %.n)] [%link ~]^%$]. It should build like this:

Copy
+$  list=jype  [[%ring [%atom jatom-type ?(%.y %.n)] [[%link ~[list]] name=%$]] name=%$]
:-  [[%atom %number %.n] name=%$]
[[%ring [%atom jatom-type ?(%.y %.n)] [[%link ~[list]] name=%$]] name=%$]
If the type of the list were previously defined (as from a type declaration), it could instead be referred to via a %link:

Copy
+$  list=jype  [[%ring [%atom jatom-type ?(%.y %.n)] [[%link ~[list]] name=%$]] name=%list]
:-  [[%atom %number %.n] name=%$]
[[%link ~[%list]] name=%$]

