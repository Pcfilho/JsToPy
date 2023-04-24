def js_to_python(js_code_to_translate):
    js_code_to_translate = remove_reserved_words(js_code_to_translate)
    js_code_to_translate = change_comparison_operators(js_code_to_translate)
    js_code_to_translate = change_incremental_operators(js_code_to_translate)

    js_code_to_translate = 'def ' + js_code_to_translate.split('(', 1)[0].split()[-1] + '(' + \
                           js_code_to_translate.split('(', 1)[1]
    js_code_to_translate = js_code_to_translate.replace('}', '')
    js_code_to_translate = js_code_to_translate.replace('{', ':')
    js_code_to_translate = js_code_to_translate.replace('else if', 'elif')

    return js_code_to_translate


def remove_reserved_words(code_to_translate):
    reserved_words = {
        'var': '',
        'let': '',
        'const': '',
        'console.log': 'print',
        ';': '\n'
    }

    code_to_translate = iterate_replacing(code_to_translate, reserved_words)
    return code_to_translate


def change_comparison_operators(code_to_translate):
    comparison_operators = {
        '===': '==',
        '!==': '!='
    }
    code_to_translate = iterate_replacing(code_to_translate, comparison_operators)
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
    code_to_translate = iterate_replacing(code_to_translate, comparison_operators)
    return code_to_translate


def iterate_replacing(word: str, dic: dict[str, str]) -> str:
    for key in dic.keys():
        word = word.replace(key, dic[key])
    return word


example1 = '''
function greet(name) {
    console.log("Hello, " + name + "!");
}
greet("World");
'''

example2 = '''
let a = 1;
const b = 2;
function sum(x, y) {
    console.log(x + y);
}
sum(a, b);
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
