from simplerr import web
from models import Person

@web('/')
def index(request):
    return """
    <ul>
        <li><a href="/person/all">Show all</a>
        <li><a href="/person/first">Show first</a>
    </ul>
    """

@web('/person/all')
def person_api(request):
    return Person.select()

@web('/person/first')
def person_first(request):
    return Person.select().get()
