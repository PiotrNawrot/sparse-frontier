from .qa.qa_task import QATask
from .ruler.cwe import CommonWordTask
from .ruler.niah import NIAHTask
from .ruler.vt import VariableTrackingTask
from .story.multihop import MultiHopTask
from .story.filtering import FilteringTask
from .story.retrieval import RetrievalTask


TASK_REGISTRY = {
    "qa_quality": QATask,
    "qa_squad": QATask,
    "qa_toefl": QATask,
    "ruler_cwe": CommonWordTask,
    "ruler_niah": NIAHTask,
    "ruler_vt": VariableTrackingTask,
    "story_multihop": MultiHopTask,
    "story_filtering": FilteringTask,
    "story_retrieval": RetrievalTask,
}
