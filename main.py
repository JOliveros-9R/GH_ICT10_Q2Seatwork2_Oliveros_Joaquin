from pyscript import display, document


def getting_data(e):
 document.getElementById('display').innerHTML = ""
 Firstname = document.getElementById('firstname').value
 Lastname = document.getElementById('lastname').value
 subj1 = document.getElementById('subj1').value
 subj2 = document.getElementById('subj2').value
 subj3 = document.getElementById('subj3').value
 subj4 = document.getElementById('subj4').value
 subj5 = document.getElementById('subj5').value
 subj6 = document.getElementById('subj6').value

 
 display(f'Name: {Firstname} {Lastname}', target='display')
 display(f'English: {subj1}, Math: {subj2}, Science: {subj3}, SS: {subj4}, PE: {subj5}, TLE:{subj6}', target='display')
 
 
 
def getting_gwa(e):
 document.getElementById('display').innerHTML = ""
 subj1 = float(document.getElementById('subj1').value)
 subj2 = float(document.getElementById('subj2').value)
 subj3 = float(document.getElementById('subj3').value)
 subj4 = float(document.getElementById('subj4').value)
 subj5 = float(document.getElementById('subj5').value)
 subj6 = float(document.getElementById('subj6').value)
 add = subj1 + subj2 + subj3 + subj4 + subj5 + subj6 
 sum = add /6
 display(f'Your General Weighted Average is {sum:.2f}', target='display')

 if sum >= 75: display("Result: PASSED", target='display') 
 else: display("Result: FAILED", target='display')