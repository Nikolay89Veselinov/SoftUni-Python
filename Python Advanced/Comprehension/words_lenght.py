# Using list comprehension, write a program that receives some strings separated by comma and space &quot;, &quot; and
# prints on the console each string with its length in the format: &quot;{first_str} -&gt; {first_str_len},
# {second_str} -&gt; {second_str_len}…&quot;

print(', '.join([(f'{x} -> {len(x)}') for x in input().split(', ')]))

# input

# Peter, George, Bill, Lilly, Katy