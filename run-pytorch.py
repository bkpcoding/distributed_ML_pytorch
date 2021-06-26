# run-pytorch.py
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig

if __name__ == "__main__":
    ws = Workspace.from_config()
    experiment = Experiment(workspace=ws, name='single-cpu')
    config = ScriptRunConfig(source_directory='./example',
                             script='main.py',
                             compute_target='distbelief-single')

    # use curated pytorch environment 

    run = experiment.submit(config)

    aml_url = run.get_portal_url()
    print(aml_url)
