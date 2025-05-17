import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace

# CSV dosyasını oku
df = pd.read_csv("data_semicolon_delimited.csv", sep=';')

# RDF graph'ı oluştur
g = Graph()
EX = Namespace("http://example.org/dozent/")

# Namespace'i bind et
g.bind("ex", EX)

# Her satırı RDF triplet'lerine dönüştür
for _, row in df.iterrows():
    subject_uri = URIRef(f"{EX}{row['Dozentennummer']}")

    g.add((subject_uri, RDF.type, EX.Dozent))
    g.add((subject_uri, EX.ProsopID, Literal(row['ProsopID'])))
    g.add((subject_uri, EX.Vollname, Literal(row['Vollname'])))
    g.add((subject_uri, EX.Nachname, Literal(row['Nachname'])))
    g.add((subject_uri, EX.Vorname, Literal(row['Vorname'])))

    if pd.notna(row['Geburt']):
        g.add((subject_uri, EX.Geburt, Literal(row['Geburt'])))
    if pd.notna(row['Tod']):
        g.add((subject_uri, EX.Tod, Literal(row['Tod'])))
    if pd.notna(row['Institution']):
        g.add((subject_uri, EX.Institution, Literal(row['Institution'])))
    if pd.notna(row['Fakultaet']):
        g.add((subject_uri, EX.Fakultaet, Literal(row['Fakultaet'])))
    if pd.notna(row['Typ']):
        g.add((subject_uri, EX.Typ, Literal(row['Typ'])))
    if pd.notna(row['Beschreibung']):
        g.add((subject_uri, EX.Beschreibung, Literal(row['Beschreibung'])))
    if pd.notna(row['Von']):
        g.add((subject_uri, EX.Von, Literal(row['Von'])))
    if pd.notna(row['Bis']):
        g.add((subject_uri, EX.Bis, Literal(row['Bis'])))
    if pd.notna(row['Verwandt']):
        g.add((subject_uri, EX.Verwandt, Literal(row['Verwandt'])))

# TTL dosyasını kaydet
g.serialize(destination="dozenten.ttl", format="turtle")
