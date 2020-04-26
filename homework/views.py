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
                'students_statistics': [
                    {
                        'id': 1,
                        'fio': 'Someone',
                        'timp': 2,
                        'eis': 3,
                        'philosophy': 4,
                        'english': 5,
                        'sport': 2.3,
                        'average': 2.3,
                    }
                ],
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context

    '''
    def _generate_test_data(self):
        student = Student('Petr')
        return scores
    '''

class Student:
    pass


class Statistics:
    # student_id, [Scores]
    pass

class Subject:
    pass

class Score:
    # Subject, Student, value
    pass
