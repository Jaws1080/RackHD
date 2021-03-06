# import tests
from config_tests import ConfigTests
from nodes_tests import NodesTests
from catalogs_tests import CatalogsTests
from pollers_tests import PollersTests
from obm_tests import OBMTests
from workflows_tests import WorkflowsTests
from workflowTasks_tests import WorkflowTasksTests
from tags_tests import TagsTests
from schema_tests import SchemaTests
from lookups_tests import LookupsTests
from skupack_tests import SkusTests

tests = [
    'nodes_api2.tests',
    'config_api2.tests',
    'catalogs_api2.tests',
    'pollers_api2.tests',
    'obm_api2.tests',
    'workflows_api2.tests',
    'workflowTasks_api2.tests'
    'pollers.tests',
    'tags_api2.tests',
    'obm_api2.tests',
    'schemas_api2.tests',''
    'skus_api2.tests',
    'lookups_api2.tests'
]

regression_tests = [
]
