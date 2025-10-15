from .nodes.pipeline_loader import PipelineLoader
from .nodes.idm_vton import IDM_VTON
from .nodes.idm_vton_v2 import IDM_VTON_V2


NODE_CLASS_MAPPINGS = {
    "PipelineLoader": PipelineLoader,
    "IDM-VTON": IDM_VTON,
    "IDM-VTON_V2": IDM_VTON_V2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PipelineLoader": "Load IDM-VTON Pipeline",
    "IDM-VTON": "Run IDM-VTON Inference",
    "IDM-VTON_V2": "IDM_VTON_V2"
}