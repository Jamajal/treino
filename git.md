## Git

### Funcionamento

O Git é um sistema de controle de versão distribuído que permite que você acompanhe as alterações feitas em arquivos ao longo do tempo. Com o Git, você mantém um repositório de código-fonte em sua máquina local. Este repositório contém todas as versões do seu projeto ao longo do tempo, permitindo que você reverta para versões anteriores, acompanhe o histórico de alterações e colabore com outros desenvolvedores.

As alterações no seu código são registradas através de commits. Um commit é uma captura de uma versão específica do seu projeto, acompanhada de uma mensagem que descreve as alterações feitas. O Git permite que você crie branches (ramificações) do seu código. Cada branch representa uma linha de desenvolvimento separada, o que é útil para trabalhar em novos recursos ou correções de bugs sem afetar o código principal.

Depois de fazer alterações em uma branch, você pode mesclar (merge) essas alterações de volta para o branch principal. Isso permite que várias pessoas trabalhem em partes diferentes do código simultaneamente, mantendo tudo sincronizado.

### Github

O GitHub é uma plataforma de hospedagem de repositórios Git na nuvem. Ele permite que você armazene seus repositórios Git de forma remota, tornando-os acessíveis a outros desenvolvedores e facilitando a colaboração em projetos de código aberto ou privados.

Dessa forma, nós temos um repositório local, que é o repositório git na nossa máquina e temos também o repositório remoto do GitHub e podemos sincronizá-los para manter o armazenamento em nuvem, muito mais seguro dessa forma.

### Credênciais

Ao utilizar o git no terminal, eventualmente será solicitado a realização do login. Para isso basta estar logado no github e utilizar os seguintes comandos no terminal:

```
git config --globa user.name "(Usuário do github)"
```

```
git config --globa user.email "(Email do github)"
```

## Inicializando um repositório

De modo geral a duas maneiras de você inicializar um repositório git em sua máquina. Isso pode ser feito da nuvem para a máquina local ou o contrário, acredito que a primeira opção é muito mais prática.

### Nuvem para máquina local

Com esta estratégia você deve ir até o site do github e inicalizar um novo repositório. É bem fácil e prático, as configurações mais importantes são nome, descrição (opcional), se será público ou privado e se terá o README incluso.

Após a criação do repositório sincronizar ele com o repositório local da nossa máquina que ainda não existe. Se você tiver adicionado um README, clique no botão Code, irá aparecer um menu. Certifique-se de estar com a opção http selecionada e copie o link terminado em .git que cosntar no menu.

Se você não tiver adicionado um REAME, o botão Code não estará aparecendo, mas o link estará disponível em um componente chamado Quick Setup na tela.

Tendo encontrado e copiado esse link, basta você abrir o seu terminal, navegar até a pasta que deseja armazenar o repositório git e rodar o seguinte comando:

```
git clone (link gerado pelo github)
```

Esse comando irá criar uma nova pasta com o nome que você escolheu para o repositório do github. Esta pasta estará exatamente igual ao estado atual do repositório do github + um arquivo .git, este arquivo é o que permite o git mapear seu repositório local.

Agora quaisquer alterações que você fizer na sua máquina local, você enviar para o repositório remoto do GitHub. Basta realizar esta sequência de comandos sempre que quiser fazer uma nova atualização:

```
git add *
```

Este comando usado para adicionar mudanças a área de preparação do Git (Ainda não ao repositório remoto). Essas mudanças são preparadas para serem incluídas no próximo commit. Você pode adicionar arquivos individualmente ou usar curingas para adicionar várias alterações de uma vez. O símbolo \* ou . adiciona todas as alterações para a preparação, contudo se você quiser adicionar somente um arquivo especifico, pode apenas informar o nome dele na frente do add.

```
git commit -m (Título do commit)
```

Este comando é usado para criar um snapshot permanente das mudanças que estão no índice. Um commit é uma captura de uma versão específica do seu projeto, acompanhada de uma mensagem descritiva que explica as alterações feitas.

```
git push
```

Este comando é usado para enviar commits locais para um repositório remoto, como o GitHub. Ele atualiza o repositório remoto com as alterações que você fez localmente.

## Outros comandos importantes

```
git pull
```

Caso esteja trabalhando em um repositório que possui outros colaboradores, é interessante o uso do comando acima sempre que você for começar a desenvolver alguma alteração, ele irá baixar as alterações feitas pelos colaboradores para seu repositório local.

```
git branch
```

O comando git branch é usado para listar, criar ou excluir branches no repositório Git. Sem argumentos, ele lista todos os branches presentes no repositório, indicando qual branch é o atual (com um asterisco).

```
git branch (nome da nova branch)
```

Cria um novo branch com o nome especificado.

```
git branch -d (nome da nova branch)
```

Exclui o branch com o nome especificado.

```
git checkout
```

Este comando é usado para alternar entre branches ou para restaurar arquivos do diretório de trabalho para o estado em que estavam em um commit específico. Quando usado para alternar entre branches, você fornece o nome do branch para o qual deseja mudar.Quando usado para restaurar arquivos, você fornece o nome do arquivo ou uma referência de commit.

```
git checkout -- (nome do arquivo)
```

Restaura o arquivo para o estado em que estava no último commit, o nome do arquivo pode ser substituído por \* para restaurar todos os arquivos. É válido ressaltar que todas as alterações feitas em sua máquina local serão descartadas ao restaurar um arquivo.

```
git status
```

Este comando mostra o estado atual do repositório Git, incluindo quais arquivos foram modificados, quais estão sendo rastreados ou não rastreados, e em qual branch você está. Ele fornece informações sobre o que está acontecendo no seu diretório de trabalho em relação ao repositório Git.
