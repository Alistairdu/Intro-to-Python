'''
print() -> writes to output/console

Data class: 
    type() ->
        int - int() etc.
        float
        bool
        str
        list ~ array
            range - range() -> subset of list
        None = null/nothing/undefined/ N/A
            int(2.3) = 2; casts 2.3 to class int; can be done with all types!
                use round(2.3) = 2.0 to stay in float/for cleanliness
            bool(2.3) = true -> truthy. 0 & "" = false -> falsy

Arithmatic Operators: 
    follow pemd%as
    * / + - = mdas
            * / 
        -> float
            + - 
            % = mod
            ** = exponential
            / / = floor division (knocks off remainder)
        -> float if either = float, otherwise = int
    Booleans: True = 1; False = 0; and, or, not - !
        -> use operators <, >, <>, ==, != etc. with these
    Bitwise logical operators: use on integers
        follow ~ & ^ | 
            -> and before logical operators not, and, or
        & = and -> true if both statements = True, False otherwise
        | = or -> false if both statements = False, True otherwise
        ~ = not -> flips whatever follows - not True = False, etc. 
        ^ = Exclusive OR 
            -> True if True/False, or False/True, False otherwise
            <, >, <>, >= -> bool

Incrementation: 
    a *= 5 -> a = a * 5

Comments: 
    # = line comment
    3 " or ' = block comments

Blocks:
    groups of statements are put together by indenting; tab = 4 spaces. 
    The indented statement will only run if statement above it 
        is true/satisfied
    def indent(x):
        if same block:
            indent
        elif different block:
            don't indent
        else: 
            indent




Functions: 
    def sample fuction(x): (functin with no paramaters = "fn():")
        return gives output
            if no 'return', returns "None"
        paramater = x above - a variable only accessable within the fuction
            argument = specific value assigned to a paramater eg. 12
        looks for/uses local varibles before global variables
    if there is no 'return' at the end of a fn, returns 'None' type
    
    input(menu txt before input prompt) - takes input from user as a 'string'
    abs(#) -> absolute value 
    round(float) -> rounds to whole #
    len(str) = length of string 
    str1 + str2 == str1*2 == str1str2 -> to concatenate strings
    print(f'this is an f-string with {variable1}')
    range(start, stop, increment), 
    range(5) -> [0,1,2,3,4]
    range(2,5) -> [2,3,4]
    isinstance(x, int) -> bool with whether x is an int
    sorted(list) = sorts list small to large. list must be all 
        integers/floats or 
        strings(sorts by alphabetical ordrer, wtih CAPS before non-caps)
        to reverse sort -> 
    sorted(list,reverse = True) to reverse a sorted list
        Does not change underlying object
    reversed(list) - reverses order of list - but returns reverse object
        so must make that back into a list to view -> list(reverse object)
            Does not change underlying object
    sum(sum of eles in list)
    max(list); useful in list.remove(max(list)) -> for #s or strings
    min(list)
    any(list) - > returns True if any True(thy) value in list: like OR
    all(list) - > returns True if all True(thy) objects in list: like AND
        use on a list/dictionary to make sure there is data in each bucket
    choice(lst, tuple, or str) -> returns random ele
        -> get from random library by: 'from random import choice' above
    
    Methods are features called from within an object and 
        functions are applied to an object

Variables: convention says use well-defined and succinct snake_case names 
    id(x) -> Location of x
    when x changed/updated -> new id/location because it is actually being 
        re-assigned, NOT updated
    id of any output - e.g. integer 4, will never change during any single 
        instance of Python;
        so if x = 4, y = 4, id(x) == id(y)
    assign with =
        x = 2
        a,b = 1,2 - multiple in one line
        y = (1,2,3) - unpacking
        g,h,i = y - packing
        j = k = l = m = n = 0 - assign multile same value
    don't write code that relies on global variables ;)
        An object is some memory that holds a value of a given type
            A variable is a named object/a name pointing at an object




Scalar Types: are IMMUTABLE in Python
    thse are classes that are sinlge entities - int, float, bool, str, None

Collection Types: 
    MUTABLE
        list [x,7, 'fds']
        dict = dictionary
    IMMUTABLE
        tuple: a special list used in enumerate() & zip() eg(1,'a', 2.0)

Indexing: 
    "str"[1] = t -> input must be integer
    [1,2,3,"list"][-1] = "list" -> -1 = last element

Underflow:
    since floats aren't stored as direct representations of their binary 
    form like integers float will only be accurate to a certain # of 
    decimal places, potentially causing problems

Lists: 
    An orered set of elements that may contain other lists as elements
    listy = ['elephant,1,True] flexible, indexed arrays containing 
        elements or values
    list(produces a list)
    [a,b,c]
    [a] * 4 = [a,a,a,a]
    listy.append(ele)
    unpack lists by: 1, 2, 3, 4 = listy; 
        1,2,3,4 are new variables
        print(3) = True
        print(4) = ele
    'in' used to check whether element is in a list: 
        'True' in listy -> Boolean (True here) 
        'not in' possible too
    Slice list - take a piece of it using it's index:
        listy[1:] -> [1,True, ele] - takes index 1 to the end of the list
        listy[1:3] -> [1,True] - second figure exclusive 
        (doesn't include index 3 here)
        slice_of_list = listy[1:] -> goes to the end
        sliced_increments = listy[::2] - leaves every second ele
    If paramater of a fn is a list, since lists are MUTABLE, change paramater
            to new list before manipulating it to avoid problems. 
        3 equivalent ways to slice lists into a new memory location 
            so changes don't impact original paramater:
            lst2 = lst[:]
            lst2 = lst.copy()
            lst2 = list(lst)
    list methods: list
        .append(single_ele) -> for adding single element
        .extend(ele1, ele2, etc) - for adding multiple elements
        .remove(ele) -> removes first instance of ele
        .pop(idx) -> removes index # from list/ last entry if idx entry empty
            Can set this remved value equal to a variable
        .sort() ->sots like fuction above rearranges in place
        .reverse() reverses list in place, rearranges in place
        del list[1:2] -> deletes elements at index 1-2
        .index(ele) -> returns index # of ele
        .count(ele_to_count)
        may NOT do list.sort().reverse() 
            -> as.sort -> operates on what comes before. None comes after
Loops: 
    Rule of thumb for choosing 'for loops' vs 'while loops'
        use for loops when you know how many times to do something
        use while loops when the number of iterations needed to solve a 
            problem is unknown
                also for menus, sessions, and "wait states"
                watch out for infinite loops
    for ele in lst: 
        print(ele)
    for i, ele in enumerate(lst, start_idx):   (start_idx is optional)
    
    Boolean Flags - exit loops under given condition
        if val > 90:
            has_value_over_90 = True
            break -> exits all loops
            continue -> goes direct to next iteration of the loop you're in
            pass -> use to avoid commitiing an operation 
                i.e. as a placeholder so file will run

    Collectors => List Accumulators
        collect numbers over an iteration loop
    zip() -> parallel iteration:check each ele of both lists @ same time
            for a, b in zip(lst_a, lst_b):
                if a % 2 == 1:
                    odds.append(a)
                if b % 2 == 1:
                    odds.append(b)
        may also use if the lists are not of the same length, 
            but iteration will cease as soon as shortest list is exhausted  

    Open-ended problem (here), is any problem where you don't know how many
        iterations it will take to achieve a result.

    Menu in Command Line
        def menu_():
        menu = """
            Choose:
                1) Schnitzel
                2) Beef Bourguignon
                3) Duck au Poivre
                """
            choice = int(input(menu))
            menu_item = ['Schnitzel', 'Beef Bourguignon', 'Duck au Poivre']
            return menu_item[choice - 1]

        order = []
        cont = 'y'
        while cont == 'y':
            order.append(menu_())
            cont = input("anything else?")
        print(order) -> returns lst of order items
    








    Strings: are immutable, so new string is returned from these methods
    .upper() -> all upper-case
    .lower() -> all lower-case
    .isalnum() 
        -> returns boolean weither string is all alpha-numeric characters
            - letters & numbers
        .isalpha() -> str all letters
        .isdigit() -> str integer
    .isspace() -> str is whitespace 
                    -> space, newline /n, tab /t, carriage return /r
    .capitalize() -> capitalize the first chat of each word
    .split(",") -> splits string into list of strings (on 'space' by default)
    .join() -> list = ['I', 'love', 'you'] -> print(" ".join(list))

'''
""" """
