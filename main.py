def js_to_python(js_code_to_translate):
    js_code_to_translate = js_code_to_translate.replace('console.log', 'print')
    js_code_to_translate = js_code_to_translate.replace('var', '')
    js_code_to_translate = js_code_to_translate.replace('let', '')
    js_code_to_translate = js_code_to_translate.replace('const', '')
    js_code_to_translate = js_code_to_translate.replace('===', '==')
    js_code_to_translate = js_code_to_translate.replace('!==', '!=')
    js_code_to_translate = js_code_to_translate.replace('++', '+= 1')
    js_code_to_translate = js_code_to_translate.replace('--', '-= 1')
    js_code_to_translate = js_code_to_translate.replace('+=', '+= ')
    js_code_to_translate = js_code_to_translate.replace('-=', '-= ')
    js_code_to_translate = js_code_to_translate.replace('*=', '*= ')
    js_code_to_translate = js_code_to_translate.replace('/=', '/= ')
    js_code_to_translate = js_code_to_translate.replace('%=', '%= ')
    js_code_to_translate = js_code_to_translate.replace(';', '\n')

    js_code_to_translate = 'def ' + js_code_to_translate.split('(', 1)[0].split()[-1] + '(' + js_code_to_translate.split('(', 1)[1]
    js_code_to_translate = js_code_to_translate.replace('}', '')
    js_code_to_translate = js_code_to_translate.replace('{', ':')
    js_code_to_translate = js_code_to_translate.replace('else if', 'elif')

    return js_code_to_translate


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
