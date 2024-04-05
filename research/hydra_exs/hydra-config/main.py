import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg: DictConfig) -> None:
    assert cfg.node.loompa == 10  # attribute style access
    assert cfg["node"]["loompa"] == 10  # dictionary style access

    assert cfg.node.zippity == 10  # Value interpolation
    assert isinstance(cfg.node.zippity, int)  # Value interpolation
    assert cfg.node.do == "oompa 10"  # string interpolation

    cfg.node.waldo  # raises an Exception


if __name__ == "__main__":
    my_app()
