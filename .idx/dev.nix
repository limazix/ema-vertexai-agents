# To learn more about how to use Nix to configure your environmentn
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python3Full
    pkgs.python3Packages.pip
    pkgs.python3Packages.virtualenv
    pkgs.pipx
    pkgs.commitizen
    pkgs.python3Packages.pdm-backend
    pkgs.pdm
  ];

  # Sets environment variables in the workspace
  env = {};
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
      "charliermarsh.ruff"
      "ms-python.debugpy"
      "ms-python.python"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        web = {
          # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
          # and show it in IDX's web preview panel
          command = ["pdm" "run" "serve"];
          manager = "web";
          env = {
            # Environment variables to set for your server
            UVICORN_PORT = "$PORT";
          };
        };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        pdm-init="pdm init";
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: start a background task to watch and re-build backend code
      };
    };
  };
}
