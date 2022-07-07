import jams
jams.schema.add_namespace('pattren_rel1.json')
sample = jams.JAMS()

sample.file_metadata.title = "Shahid is a rockstar"
sample.file_metadata.release = "Give me a pattern"
sample.file_metadata.duration = 130

pattern_annotation = jams.Annotation(namespace="pattern_jku")
#print("test")
mydict = {
"pattern_id": 1,
"midi_pitch": 50,
"occurrence_id": 1,
"morph_pitch": 54,
"staff": 1
}
#pattern_annotation.time = 0
#pattern_annotation.duration = 130 # annotation covers all the score
pattern_annotation.append(time=0.0,
                   duration=0.9,
                   value=mydict,
                   confidence=1.0)
#pattern_annotation.append(value= "1")
#pattern_annotation.append(value="3")

sample.annotations.append(pattern_annotation)
sample.save("my_jams_file1.jams", strict=False)
