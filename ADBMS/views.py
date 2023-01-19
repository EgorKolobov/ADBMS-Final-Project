from django.shortcuts import render
import neo4jupyter
from py2neo import Graph
from neo4j import GraphDatabase
from pandas import DataFrame


class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


def home(request):
    return render(request, 'ADBMS/index.html')


def neo4j_query1(request):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="ekoloboff", pwd="20012001")
    query_string = '''MATCH path = (uu:USER)-[h:HAVING]->(rg:RG)-[ct:CONTAIN]->(prg:PRG)-[conn:CONNECT]->(p:PRODUCT)<-[prov:PROVIDE]-(ss:SUPPLIER {sname:"品冠行銷股份有限公司"})
    return count(path) AS CT, uu
    ORDER BY CT DESC
    LIMIT 3
    '''
    dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')]).head()
    table = dtf_data.to_html()
    g = Graph(query_string, auth=('ekoloboff', '20012001'))
    picture = neo4jupyter.draw(g, {'label_name': 'attribute_name'})
    conn.close()
    return render(request, 'ADBMS/neo4j_query1.html', {'title': 'Home', 'table': table, 'picture': picture})


def neo4j_query2(request):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="ekoloboff", pwd="20012001")
    query_string = '''
    MATCH (c:CATEGORY {class:"7308"})<-[b:BELONG]-(p:PRODUCT)<-[:PROVIDE]-(:SUPPLIER {sname:"品冠行銷股份有限公司"})
    RETURN c,b,p
    '''
    dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')]).head()
    table = dtf_data.to_html()
    g = Graph(query_string, auth=('ekoloboff', '20012001'))
    picture = neo4jupyter.draw(g, {'label_name': 'attribute_name'})
    conn.close()
    return render(request, 'ADBMS/neo4j_query2.html', {'title': 'Home', 'table': table, 'picture': picture})


def neo4j_query3(request):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="ekoloboff", pwd="20012001")
    query_string = '''
    match (:SUPPLIER {sname:"品冠行銷股份有限公司"}) -[:PROVIDE]->(p:PRODUCT)<-[conn:CONNECT]-(:PRG)<-[ct:CONTAIN]-(:RG) 
    return p, count(ct) as degree
    ORDER BY degree DESC
    LIMIT 1
    '''
    dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')]).head()
    table = dtf_data.to_html()
    g = Graph(query_string, auth=('ekoloboff', '20012001'))
    picture = neo4jupyter.draw(g, {'label_name': 'attribute_name'})
    conn.close()
    return render(request, 'ADBMS/neo4j_query3.html', {'title': 'Home', 'table': table, 'picture': picture})


def neo4j_query4(request):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="ekoloboff", pwd="20012001")
    query_string = '''
    MATCH (s:SUPPLIER)-[:PROVIDE]->(:PRODUCT)-[t:BELONG] -(c:CATEGORY)
    return s.sname AS name, collect(DISTINCT c.class_name) AS sells
    '''
    dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')]).head()
    table = dtf_data.to_html()
    g = Graph(query_string, auth=('ekoloboff', '20012001'))
    picture = neo4jupyter.draw(g, {'label_name': 'attribute_name'})
    conn.close()
    return render(request, 'ADBMS/neo4j_query4.html', {'title': 'Home', 'table': table, 'picture': picture})


def neo4j_query5(request):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="ekoloboff", pwd="20012001")
    query_string = '''
    MATCH (c:USER)-[h:HAVING]->(:RG)-[ct:CONTAIN]->(:PRG)-[:CONNECT]->(:PRODUCT)-[:BELONG]->(cat:CATEGORY)
    return cat.class_name AS purchase, count(ct) AS quantity
    ORDER by quantity
    DESC
    '''
    dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='neo4j')]).head()
    table = dtf_data.to_html()
    g = Graph(query_string, auth=('ekoloboff', '20012001'))
    picture = neo4jupyter.draw(g, {'label_name': 'attribute_name'})
    conn.close()
    return render(request, 'ADBMS/neo4j_query5.html', {'title': 'Home', 'table': table, 'picture': picture})


def postgresql_query1(request):
    return render(request, 'ADBMS/postgresql_query1.html', {'title': 'Home'})


def postgresql_query2(request):
    return render(request, 'ADBMS/postgresql_query2.html', {'title': 'Home'})


def postgresql_query3(request):
    return render(request, 'ADBMS/postgresql_query3.html', {'title': 'Home'})
