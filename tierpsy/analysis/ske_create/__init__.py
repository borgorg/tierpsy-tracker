from .getSkeletonsTables import trajectories2Skeletons

def args_(fn, param):
    #arguments used by AnalysisPoints.py
    return {
        'func': trajectories2Skeletons,
        'argkws': {**{'skeletons_file': fn['skeletons'], 
                    'masked_image_file': fn['masked_image']}, 
                    **param.skeletons_param},
        'input_files' : [fn['masked_image']],
        'output_files': [fn['skeletons']],
        'requirements' : ['SKE_INIT'],
    }