def js_to_python(js_code_to_translate):
    remove_reserved_words(js_code_to_translate)
    change_comparison_operators(js_code_to_translate)
    change_incremental_operators(js_code_to_translate)

    js_code_to_translate = 'def ' + js_code_to_translate.split('(', 1)[0].split()[-1] + '(' + \
                           js_code_to_translate.split('(', 1)[1]
    js_code_to_translate = js_code_to_translate.replace('}', '')
    js_code_to_translate = js_code_to_translate.replace('{', ':')
    js_code_to_translate = js_code_to_translate.replace('else if', 'elif')

    return js_code_to_translate


def remove_reserved_words(code_to_translate):
    variable_reserved_words = ['var', 'let', 'const']

    reserved_words = {
        'console.log': 'print',
        ';': '\n'
    }

    for word in variable_reserved_words:
        code_to_translate.replace(word, '')

    for operator in reserved_words.keys():
        code_to_translate.replace(operator, reserved_words[operator])
    return code_to_translate


def change_comparison_operators(code_to_translate):
    comparison_operators = {
        '===': '==',
        '!==': '!='
    }
    for operator in comparison_operators.keys():
        code_to_translate.replace(operator, comparison_operators[operator])
    return code_to_translate


def change_incremental_operators(code_to_translate):
    comparison_operators = {
        '++': '+= 1',
        '--': '-= 1',
        '*=': '*= ',
        '/=': '/= ',
        '%=': '%= ',
        '+=': '+= ',
        '-=': '-= ',
    }
    for operator in comparison_operators.keys():
        code_to_translate.replace(operator, comparison_operators[operator])
    return code_to_translate


example1 = '''
function greet(name) {
    console.log("Hello, " + name + "!");
}
greet("World");
'''

example2 = '''
function sum(x, y) {
    console.log(x + y);
}
sum(2, 2);
'''

example3 = '''
function checkThis(a, b) {
    if (a === b) {
        console.log("Foi")
    }else if (a > b){ 
        console.log("a maior que b")

    }else {
        console.log("Nao Foi")
    }
}
checkThis(2, 1);
'''

example4 = '''
function greet(name) {
    console.log("Hello, " + name + "!");
}
greet("World");
'''

example5 = '''
function greet(name) {
    console.log("Hello, " + name + "!");
}
greet("World");
'''

py_code = js_to_python(example3)

print(py_code)
exec(py_code)
