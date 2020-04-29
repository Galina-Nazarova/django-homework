# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        '''
        student = Student('Petr')
        statistics = Statistics(scores)
        context.update(
            {
                'students_statistics': bad_students.get_data(),
                'excellent_students': statistics.get_exelent_students(),
                'bad_students': statistics.get_bad_students()
            }
        )
        проверка
        '''

        context.update(
            {
                'students_statistics': students.get_data(),
                'excellent_students': students.get_exelent_student(),
                'bad_students': students.get_bad_students()
            }
        )
        return context


'''
    def _generate_test_data(self):
        student = Student('Petr')
        return scores
'''




class Student:
    def __init__(self, subject, data):
        self.data_list = data
        self.subjects = subject

    def get_data(self):      # Добавляет в словарь студента среднее значение по оценкамт
        for data_list_item in self.data_list:
            score_values = []
            for key in data_list_item:
                if key in self.subjects:
                    score_values.append(data_list_item[key])
            average = sum(score_values)/len(score_values)
            data_list_item['average'] = average
        return self.data_list

    def get_exelent_student(self):
        students.get_data()
        stat = [value['average'] for value in self.data_list]
        exelent_average = max(stat)
        exelent_students = [i['surname'] for i in self.data_list if i['average'] == exelent_average]

        return ''.join(exelent_students)

    def get_bad_students(self):
        students.get_data()
        bad_students = [value['surname'] for value in self.data_list if value['average'] < 3]

        return ''.join(bad_students)


    def add(self, data_add):
        self.id_add = data_add['id']
        check_data_id = True
        for i in self.data_list:
            if self.id_add == i['id']:
                check_data_id = False
        if check_data_id:
            self.data_list.append(data_add)

    def remove(self,id):
        self.id_remove = id
        for i in self.data_list:
            if self.id_remove == i['id']:
                self.data_list.remove(i)




subject = ['timp', 'eis', 'philosophy', 'english', 'sport']
data = [
    {
    'id' : 1,
    'surname' : 'Ivanov A.',
    'timp' : 2,
    'eis' : 5,
    'philosophy' : 4,
    'english' : 3,
    'sport' : 5
    },
    {
    'id' : 2,
    'surname' : 'Sannikov S.',
    'timp' : 4,
    'eis' : 5,
    'philosophy' : 3,
    'english' : 5,
    'sport' : 5
    },
{
    'id' : 3,
    'surname' : 'Dyatlov T.',
    'timp' : 2,
    'eis' : 3,
    'philosophy' : 2,
    'english' : 3,
    'sport' : 4
    }
]

students = Student(subject, data)

students.add({
    'id' : 4,
    'surname' : 'Petrov E.',
    'timp' : 2,
    'eis' : 5,
    'philosophy' : 4,
    'english' : 2,
    'sport' : 4
    })

# students.remove(2)








