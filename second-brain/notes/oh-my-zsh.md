---
id: xyo5yvxvrqr5tbo7z6o556d
title: Oh My Zsh
desc: ''
updated: 1698095203029
created: 1698095200701
---

- [Oh My Zsh](https://ohmyz.sh/) est un outil open source pour faciliter la personalisation d'un terminal `zsh`
- ## Installation
  - Pour l'installer, on copie, dans le terminal, le script [[bash]] suivant :
  - ```shell
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```
- ## Powerlevel10k
  - [Powerlevel10k](https://github.com/romkatv/powerlevel10k#installation) est unthème pour Oh My Zsh. il suffit de cloner le repo git :
  - ```shell
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
    ```
  - Set `ZSH_THEME="powerlevel10k/powerlevel10k"` in `~/.zshrc`.
