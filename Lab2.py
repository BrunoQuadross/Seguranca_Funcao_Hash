import hashlib


frases = ["A primeira das instituições criadas por Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
         "A FEI é uma Instituição vinculada estatutariamente à Companhia de Jesus",
         "Em 20 de janeiro de 1952 foi realizada a sessão solene da Congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
         "A Capela Santo Inácio de Loyola foi construída em 1978, em concreto aparente.",
         "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o Instituto de Especialização em Ciências Administrativas e Tecnológicas (IECAT) foi criado em 1981",
         "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI em 2002.",
         "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
         "Em 2016 foi realizada a primeira edição do Congresso de Inovação - Megatendências 2050.",
         "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 60 mil profissionais altamente qualificados para o setor empresarial, entre administradores, engenheiros e cientistas da computação.",
         "Em 1999 iniciam-se as atividades da Faculdade de Informática - FCI, como o curso de Ciência da Computação."]

SHA256 = ["dc22d5778028c3a9764c17f6b3525faed47acab8ce52adb974e5b4740e7df584",
        "bcdc1b145c216e7672616cd4fd65e743dcbcb7dfbd7898da207623c46608bba2",
        "ca11b74ca85c72a15d9f488eec58813a7aece4245d79b4947f34353f08f349a3",
        "2507c795af00411e4531856ac3ff6f8e1230ed2c7bce0ce625fd9253b6c1616a",
        "9203bb285e2ba6b59017b82e43a54785a068ec72c41216f2f0b40fd727630c4e",
        "44841459e6b3f2d8ef183983e9d6c196824d5fe912864c5e92ec1c205b66c3a6",
        "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        "611b412b62e3111769de22a808a266e1a80bde3b3b11d2fc5c859726d1ffb401",
        "b86e3f2658ed39384b6812464413ab931309e1cfcc5104c724b855300a1f13cb",
        "c64dca8c81cc379cc4618056e2801201882cbf53d8786dd4108c7aa9775bfa91"]

MD5 = ["1fb73598032cdddd59edbd1361eab82e",
       "8375bf9b5e583cac0480dceda0e0af32",
        "cefa90b6b32782cc41e899f8ccc3ef2c",
        "72926471d5bc7796431cbd8a46d26376",
        "736062a2b1aa98f8d841e176c2ed690a",
        "16bf5ee5409000f2700f1376b88d9f16",
        "2e20bfbece6fdc62de4c4bb80a77ba1f",
        "3217881f995a0c50201061505e4060aa",
        "82c1616d6130272adb3b4048d58296e0",
        "1013976891617a120472e629ccdf3858"]

for i in range(10):
    print("===================================================")
    print("Frase numero ",i+1,"\n")
    print(frases[i]+"\n")
    sha = hashlib.sha256()
    sha.update((frases[i]).encode('utf-8'))

    md = hashlib.md5()
    md.update((frases[i]).encode('utf-8'))
    print("---------------------------------------------------")
    if(sha.hexdigest() == SHA256[i]):
        print("A frase me SHA256 esta CERTO: ",sha.hexdigest())
    else:
         print("A frase me SHA256 esta ERRADO: ",sha.hexdigest())
    print("---------------------------------------------------")
    if(md.hexdigest() == MD5[i]):
        print("A frase me MD5 esta CERTO: ",md.hexdigest())
    else:
         print("A frase me MD5 esta ERRADO: ",md.hexdigest())
    print("---------------------------------------------------\n")

print("===================================================")