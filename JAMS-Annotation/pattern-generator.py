import jams
jams.schema.add_namespace('pattern-FONN.json')
sample = jams.JAMS()
sample.file_metadata.identifiers = {
    "music-CRE": "tune1",
    "url": "somedetail"
}
sample.file_metadata.title = "Tune1"
sample.file_metadata.release = "pattern-demo"
sample.file_metadata.duration = 130

pattern_annotation = jams.Annotation(namespace="pattern-FoNN")

pattern_annotation.annotation_metadata.annotator.name = "Danny Diamond"
pattern_annotation.annotation_metadata.data_source = "program"

pattern_annotation.annotation_metadata.corpus = "CRE"
pattern_annotation.annotation_metadata.version = 1
pattern_annotation.annotation_metadata.curator.name = "Danny Diamond"
pattern_annotation.annotation_metadata.curator.email = "d.diamond1@nuigalway.ie"

pattern_annotation.annotation_metadata.annotation_tools = "FONN-Tool"
pattern_annotation.annotation_metadata.annotation_rules = None
pattern_annotation.annotation_metadata.validation = None

pattern_dict = {
          "pattern_id": "1",
          "pattern_content": "2,7,7,7,7",
          "pattern_type": "pitch-class-values",
          "pattern_frequency": 6,
          "pattern_length": 5,
          "pattern_location": "12,28, 50, 61,100"
        }
#pattern_annotation.time = 0
#pattern_annotation.duration = 130 # annotation covers all the score
pattern_annotation.append(time=0.0,duration=0.0,value=pattern_dict, confidence=1)

pattern_dict2 = {
          "pattern_id": "2",
          "pattern_content": "4,5,6,7",
          "pattern_type": "pitch-class-values",
          "pattern_frequency": 3,
          "pattern_length": 4,
          "pattern_location": "2,34, 43"
        }
pattern_annotation.append(time=0.0,duration=0.0,value=pattern_dict2, confidence=1)

sample.annotations.append(pattern_annotation)
sample.save("demo_jams_file.jams", strict=False)