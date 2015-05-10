from behave import *
import os.path
import subprocess

@given(u'I have a {sample}')
def step_impl(context, sample):
    context.sample = sample
    assert os.path.isfile('{0}.in'.format(context.sample))

@when(u'I run the main program')
def step_impl(context):
    subprocess.call('python main.py < {0}.in > {0}.out'.format(context.sample), shell=True)

@then(u'I get output files')
def step_impl(context):
    assert os.path.isfile('{0}.out'.format(context.sample))

@then(u'the output files are same as expected files')
def step_impl(context):
    f1 = open('{0}.out'.format(context.sample))
    f2 = open('{0}.expected'.format(context.sample))

    file1lines = f1.readlines()
    file2lines = f2.readlines()

    assert len(file1lines) == len(file2lines)

    for i in range(0, len(file1lines)):
        print (file1lines[i] + file2lines[i])
        assert file1lines[i] == file2lines[i]

