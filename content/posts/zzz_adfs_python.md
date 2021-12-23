sudo apt install build-essential zlib1g-dev libbz2-dev libssl-dev \
    libsqlite3-dev sqlite libffi-dev libbson-dev -y

// add python plugin
asdf plugin add python


// install python
➜  ~ asdf install python 3.9.1

➜  ~ asdf global python 3.9.1
➜  ~ python --version
Python 3.9.1

➜  ~ asdf uninstall python 3.9.1

asdf plugin-add java https://github.com/halcyon/asdf-java.git

➜  ~ asdf list-all java | grep openjdk-11.0.2

➜  ~ asdf install java adoptopenjdk-11.0.2+9

asdf global java adoptopenjdk-11.0.2+9k

For JAVA_HOME
. ~/.asdf/plugins/java/set-java-home.zsh
