import streamlit as st

if 'logged_in' not in st.session_state:
  st.session_state.logged_in = False

if 'usuario' not in st.session_state:
  st.session_state.usuario = None

print(st.session_state.usuario)

if not st.session_state.logged_in:
  pg = st.navigation([st.Page("geral/login.py", title="Login", icon=":material/login:", default=True),])
elif st.session_state.logged_in and st.session_state.usuario['administrador']:
  pg = st.navigation({
    "Conta": [
      st.Page("geral/logout.py", title="Logout", icon=":material/logout:"),
    ],
    "Bookmarks": [
      st.Page("bookmarks/list_bookmarks.py", title="Listar Bookmarks", icon=":material/bookmark:"),
      st.Page("bookmarks/create_bookmark.py", title="Criar Bookmark", icon=":material/bookmark_add:"),
      st.Page("bookmarks/remove_bookmark.py", title="Remover Bookmark", icon=":material/bookmark_remove:"),
    ],
    "Usuários": [
      st.Page("usuarios/listar_usuarios.py", title="Listar Usuários", icon=":material/group:"),
      st.Page("usuarios/criar_usuario.py", title="Cadastrar usuário", icon=":material/person_add:"),
      st.Page("usuarios/editar_usuario.py", title="Editar usuário", icon=":material/person_edit:"),
      st.Page("usuarios/remover_usuario.py", title="Remover usuário", icon=":material/person_add:")
    ],
    "Escolas":[
      st.Page("escolas/escolas.py", title="Escolas", icon=":material/dashboard:"),
      st.Page("escolas/mapa.py", title="Mapa", icon=":material/dashboard:", default=True),
      st.Page("escolas/turmas_por_escola.py", title="Turmas", icon=":material/dashboard:"),
      st.Page("escolas/alunos_professores_por_escola.py", title="Alunos, Professores e Turmas", icon=":material/dashboard:"),
      st.Page("escolas/professores_e_alunos_por_escola.py", title="Professores e Alunos", icon=":material/dashboard:"),
      st.Page("escolas/alunos_por_nivel_de_ensino.py", title="Alunos por Nível", icon=":material/dashboard:"),
    ]
  })
else:
  pg = st.navigation({
    "Conta": [
        st.Page("geral/logout.py", title="Logout", icon=":material/logout:"),
    ],
    "Escolas":[
        st.Page("escolas/escolas.py", title="Escolas", icon=":material/dashboard:"),
        st.Page("escolas/mapa.py", title="Mapa", icon=":material/dashboard:", default=True),
        st.Page("escolas/turmas_por_escola.py", title="Turmas", icon=":material/dashboard:"),
        st.Page("escolas/alunos_professores_por_escola.py", title="Alunos, Professores e Turmas", icon=":material/dashboard:"),
        st.Page("escolas/professores_e_alunos_por_escola.py", title="Professores e Alunos", icon=":material/dashboard:"),
        st.Page("escolas/alunos_por_nivel_de_ensino.py", title="Alunos por Nível", icon=":material/dashboard:"),
    ]
  })

pg.run()
