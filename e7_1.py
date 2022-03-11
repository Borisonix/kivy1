import kivy

kivy.require('1.0.8')
import openpyxl
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import runTouchApp


class AllApp(App):
    layout = BoxLayout(orientation='horizontal')
    layout_questions = GridLayout(cols=1, size_hint=(None, None), width=400, height=5500)

    def get_questions(self, subject):
        print(subject)
        wb = openpyxl.load_workbook('data.xlsx')
        sheet = wb[subject]
        data = []
        for row in range(2, sheet.max_row + 1):
            question = sheet.cell(row=row, column=1).value
            data.append(question)
        return self.add_questions(data)

    def add_questions(self, data):
        self.layout_questions.clear_widgets()
        for question in data:
            question = Button(text=question, size=(480, 40), size_hint=(1, None))
            self.layout_questions.add_widget(question)

    def build(self):
        layout_subjects = GridLayout(cols=1, size_hint=(None, None), width=400, height=1000)
        subjects = ['Logic Building',
                    'SQL Server',
                    'Advanced Excel',
                    'Programming in Java',
                    'HTML5, CSS, JavaScript, JQuery',
                    'Web Development using Servlet and JSP',
                    'Android Development using Java',
                    'Hibernate, Spring and JSF',
                    'Application Testing using JUnit ',
                    'Programming using C# ',
                    'Web development using .Net Framework',
                    'Cross Platform app for Microsoft PlayStore',
                    'distributed application with .net framwork',
                    'Machine Learning using python',
                    'Big Data using R and Python']
        subjects_d = {}
        for subject in subjects:
            subjects_d[subject] = subject
        print(subjects_d)
        for k, v in subjects_d.items():
            k = Button(text=v, size=(480, 40), size_hint=(1, None))
            k.bind(on_press=lambda k: self.get_questions(k.text))
            layout_subjects.add_widget(k)
        root = BoxLayout()
        scroll_subject = ScrollView(size_hint=(1, 1))
        scroll_question = ScrollView(size_hint=(1, 1))
        root.add_widget(self.layout)
        self.layout.add_widget(scroll_subject)
        scroll_subject.add_widget(layout_subjects)
        self.layout.add_widget(scroll_question)
        scroll_question.add_widget(self.layout_questions)
        # runTouchApp(scroll_subject)
        # runTouchApp(scroll_question)
        return root


if __name__ == '__main__':
    AllApp().run()
