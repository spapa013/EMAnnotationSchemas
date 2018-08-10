from emannotationschemas.base import BoundSpatialPoint, AnnotationSchema
import marshmallow as mm

class PhysiologyCellIDLocal( AnnotationSchema, BoundSpatialPoint ):

    cell_id = mm.fields.Int( 
                required=True,
                description='Cell id in calcium data')

    @mm.post_load
    def validate_type( self, item):
        assert item['type'] = 'physiology_cell_id'