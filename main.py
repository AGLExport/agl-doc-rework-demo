"""Release variables used by the imported AGL Markdown pages."""
def define_env(env):
    agl = env.variables["agl"]
    kind = env.variables["artifact_kind"]
    ref = agl["codename"] if kind == "release" else "master"
    env.variables["agl_download_base"] = (
        f"https://download.automotivelinux.org/AGL/{kind}/{ref}"
    )
