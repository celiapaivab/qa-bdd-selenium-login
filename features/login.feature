Feature: Login no sistema

  Scenario: Login com sucesso
    Given que estou na página de login
    When preencho o campo usuário com "usuario_teste"
    And preencho o campo senha com "senha123"
    And clico no botão de login
    Then devo ver a página inicial com a mensagem "Bem-vindo, usuario_teste"
