import ipywidgets as widgets
import requests
import time
from IPython.display import clear_output, display, Javascript


class Submission(object):
    ENDPOINT = 'https://bbp.epfl.ch/edx-single-cell/answer'

    def __init__(self):
        style = widgets.HTML('''<style>
            .custom-inputs .errors { color: #d9534f; font-size: 14px; }
            .custom-inputs .logs { margin: 10px 0 0 90px; }
            .custom-inputs .success { color: #468d89; }
            .custom-inputs .form-control { width: 80%; margin-bottom: 10px; }
            .custom-inputs .answers { font-size: 18px; margin-top: 10px; }
        </style>''')

        self.messages = widgets.HTML()

        output = [style]

        # check if the submission information was set correctly
        if not 'userid' in globals() or not 'exerciseid' in globals():
            self.show_message('User or Exercise were not setup correctly', 'errors')
            output.append(self.messages)

        else:
            self.button = widgets.Button(
                description='Submit results',
                button_style='info',
                icon='check',
                layout=widgets.Layout(margin='10px 0px 0px 75px')
            )
            self.button.on_click(self.submit_answer)
            
            self.answer_input = widgets.Textarea(
                value='',
                placeholder='Paste answer(s)',
                description='Answer:',
                layout=widgets.Layout(width='99%')
            )

            self.answers_list = widgets.HTML() # to always keep on top

            output.append(self.answer_input)
            output.append(self.button)
            output.append(self.answers_list)
            output.append(self.messages)

        self.inputs = widgets.VBox(
            children=output,
            layout=widgets.Layout(margin='10px 0px 10px 0px')
        )
        self.inputs.add_class('custom-inputs')
        display(self.inputs)

    def submit_answer(self, value):
        self.messages.value = ''

        answers = self.answer_input.value

        if not answers:
            return self.show_message('Answer(s) missing. Please fill the '
                                     'answer field and try again', 'errors')

        self.show_answers(answers)
        self.show_message('Submitting...')

        data = {'answer': answers, 'userid': userid, 'exerciseid': exerciseid}

        try:
            response = requests.post(self.ENDPOINT, json=data)
        except ValueError:
            return self.show_message('Error sending the answers', 'errors', append=True)
        else:
            if response.status_code == requests.codes.ok:
                grade = response.json()['grade']
                self.show_message('Your answer was submitted successfully!','success')
                self.show_message('<p>GRADE: %s</p>' % grade['value'], append=True)
                if 'feedback' in grade:
                    self.show_message('<p>FEEDBACK: %s</p>' % grade['feedback'], append=True)    
                self.show_message('<p>Your grade is also available on https://edge.edx.org<br>'
                                  , append=True)
            else:
                self.show_message(response.json()['message'], 'errors')

    def show_message(self, message, type_message='', append=False):
        msg = '<div class="logs %s">%s</div>' % (type_message, message)
        if append:
            self.messages.value += msg
        else:
            self.messages.value = msg

    def show_answers(self, answers):
        msg = '<div class="logs answers">Your answer(s): %s</div>' % answers
        self.answers_list.value = msg

# set the variables for submission
display(Javascript('''
    var userId = IPython.notebook.metadata.userid
    var exerciseId = IPython.notebook.metadata.exerciseid
    IPython.notebook.kernel.execute('userid = ' + userId);
    console.log(`U: ${userId} E: ${exerciseId}`);
    IPython.notebook.kernel.execute('exerciseid = ' + exerciseId);
'''))
