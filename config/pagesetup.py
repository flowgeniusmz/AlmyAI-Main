import streamlit as st
from streamlit_extras.stylable_container import stylable_container as sc

def get_page_styling():
    with open("config/style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

def get_pageconfig_item(varPageNumber: int, varPageConfigType: str):
    """
    Retrieves configuration data for a given page number and configuration type from an array within Streamlit secrets.

    Args:
    - varPageNumber: int, the page number for which to retrieve the configuration.
    - varPageConfigType: str, the type of configuration to retrieve ('title', 'subtitle', 'description', 'header', 'icon', 'path', 'about').

    Returns:
    - str, the configuration data for the given page number and configuration type from the specified array.
    """

    if varPageConfigType == "icons" :
        values = st.secrets.pageconfig.page_icons
        value = values[varPageNumber]
    elif varPageConfigType == "titles":
        values = st.secrets.pageconfig.page_titles
        value = values[varPageNumber]
    elif varPageConfigType == "subtitles":
        values = st.secrets.pageconfig.page_subtitles
        value = values[varPageNumber]
    elif varPageConfigType == "paths":
        values = st.secrets.pageconfig.page_paths
        value = values[varPageNumber]
    elif varPageConfigType == "headers":
        values = st.secrets.pageconfig.page_headers
        value = values[varPageNumber]
    elif varPageConfigType == "descriptions":
        values = st.secrets.pageconfig.page_descriptions
        value = values[varPageNumber]
    elif varPageConfigType == "abouts":
        values = st.secrets.pageconfig.page_abouts
        value = values[varPageNumber]
    else:
        value = "error"

    return value

def get_pageconfig(varPageNumber: int):
    title = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="titles")
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    path = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="paths")
    icon = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="icons")
    header = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="headers")
    description = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="descriptions")
    about = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="abouts")

    return title, subtitle, path, icon, header, description, about

def get_pageconfig_title(varPageNumber: int, varDiv: bool=True):
    title = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="titles")
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#7AB3BA;">{title} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
    if varDiv:
        st.divider()


def get_pageconfig_title_with_home_link(varPageNumber: int, varDiv: bool=True):
    
    cols = st.columns([1, 10,4,2,1]) ##7ab3ba ##4A90E2
    with cols[1]:
        title = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="titles")
        subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
        st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color: #7ab3ba;">{title} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
    with cols[3]:
        if  varPageNumber != 0:
            st.page_link(page="pages/1_🏠_Home.py", label="Home 🏠")
    if varDiv:
        st.divider()


def set_title_manual(varTitle, varSubtitle, varDiv: bool=True):
    st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#7ab3ba;">{varTitle} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{varSubtitle}</span>""", unsafe_allow_html=True)
    if varDiv:
        st.divider()
        
        
def get_component_pagelink(varPageNumber: int):
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    icon = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="icons")
    path = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="paths")
    about = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="abouts")
    page_link_container = st.container(border=False)
    with page_link_container:
        page_link = st.page_link(page=path, label=subtitle, icon=None)
        page_link_about = st.expander(label="About", expanded=False)
        with page_link_about:
            st.markdown(body=about)

def get_component_pagelink_styled(varPageNumber: int):
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    icon = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="icons")
    path = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="paths")
    about = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="abouts")
    #page_link_container = st.container(border=False)
    container = st.container(border=False, height=250)
    with container:
        page_link = st.page_link(page=path, label=subtitle, icon=None)
        page_link_container = container_styled2(varKey=f"page{varPageNumber}")
        with page_link_container:
            #page_link = st.page_link(page=path, label=subtitle, icon=None)
            page_link_about = st.expander(label="About", expanded=True)
            with page_link_about:
                st.markdown(body=about)
            cols = st.columns([1, 2, 4, 2, 1])
            with cols[2]:
                navigate_button = st.button(label="Click Here to View", use_container_width=True, key=f"pagelinkbutton_{varPageNumber}")
                if navigate_button:
                    st.switch_page(page=path)

def get_component_pagelink_styled_popover(varPageNumber: int):
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    icon = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="icons")
    path = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="paths")
    about = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="abouts")
    #page_link_container = st.container(border=False)
    #container = container_styled2A(key=f"dafdaadfa_{varPageNumber}")
    container = container_styled2(varKey=f"dfsd_{varPageNumber}")
    with container:
        #pagelink = st.page_link(page=path, label=subtitle, icon=None, use_container_width=True)
        container1 = container_styled3(varKey=f"dsa_{varPageNumber}")
        with container1:
            pagelink = st.page_link(page=path, label=subtitle, icon=None, use_container_width=True)
            pop = st.popover(label="About", disabled=False, use_container_width=True)
            with pop:
                st.markdown(about)


def get_component_pagelinksection():
    link_container = st.container(border=False)
    with link_container:
        link_columns_row1 = st.columns([1,20,20,1])
        with link_columns_row1[1]:
            get_component_pagelink_styled(1)
            get_component_pagelink_styled(3)
        with link_columns_row1[2]:
            get_component_pagelink_styled(2)
            get_component_pagelink_styled(4)

def get_component_pagelinksection_styled():
    link_container = st.container(border=False)
    with link_container:
        link_columns_row1 = st.columns([1,20,20,1])
        with link_columns_row1[1]:
            get_component_pagelink_styled(1)
            get_component_pagelink_styled(3)
        with link_columns_row1[2]:
            get_component_pagelink_styled(2)
            get_component_pagelink_styled(4)

def get_component_pagelinksection_styled_popover():
    link_container = st.container(border=False)
    with link_container:
        link_columns_row1 = st.columns([1,20,20,1])
        with link_columns_row1[1]:
            get_component_pagelink_styled_popover(1)
            get_component_pagelink_styled_popover(3)
        with link_columns_row1[2]:
            get_component_pagelink_styled_popover(2)
            get_component_pagelink_styled_popover(4)

        

def get_component_overview(varPageNumber: int):
    header = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="headers")
    subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
    description = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="descriptions")
    st.markdown(f"""<span style="font-weight: bold; color:#4A90E2; font-size:1.3em;">{header}</span>""", unsafe_allow_html=True)    
    if varPageNumber == 0:
        st.markdown(body=description)
    else:
        st.markdown(f"{description}")
    st.divider()

def display_background_image():
    # Set the Streamlit image for branding as the background with transparency
    background_image = 'https://almainc.com/sites/default/files/alma-nav-logo-r.svg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.90)), url({background_image});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def display_background_image2():
    # Set the Streamlit image for branding as the background with transparency
    background_image = 'https://almainc.com/sites/default/files/alma-nav-logo-r.svg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.9)), url('{background_image}');
            background-size: cover;
            background-attachment: fixed; /* Ensures the background is fixed during scroll */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def create_sidebar_nav(varPageNumber: int):
    st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=0, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=0, varPageConfigType="subtitles"), disabled=(varPageNumber == 0))
    st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=1, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=1, varPageConfigType="subtitles"), disabled=(varPageNumber == 1))
    st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=2, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=2, varPageConfigType="subtitles"), disabled=(varPageNumber == 2))
    st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=3, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=3, varPageConfigType="subtitles"), disabled=(varPageNumber == 3))
    st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=4, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=4, varPageConfigType="subtitles"), disabled=(varPageNumber == 4))
    #st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=5, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=5, varPageConfigType="subtitles"), disabled=(varPageNumber == 5))
    #st.sidebar.page_link(page=get_pageconfig_item(varPageNumber=6, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=6, varPageConfigType="subtitles"), disabled=(varPageNumber == 6))


def get_blue_header(varText: str):
    st.markdown(f"""<span style="font-weight: bold; color:#7ab3ba; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)    

def get_gray_header(varText: str):
    st.markdown(f"""<span style="font-weight: bold; color:#333333; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)

def get_green_header(varText: str):
    st.markdown(f"""<span style="font-weight: bold; color:#00b084; font-size:1.3em;">{varText}</span>""", unsafe_allow_html=True)
    
    
def get_sidebar_pagelinks():
    page_paths = st.secrets.pageconfig.page_paths
    page_subtitles = st.secrets.pageconfig.page_subtitles
    page_total_count = st.secrets.pageconfig.page_count
    # Corrected the loop to use Python's range for iteration
    for i in range(page_total_count):
        path = page_paths[i]
        subtitle = page_subtitles[i]
        sidebar = st.sidebar
        with sidebar:
            st.page_link(page=path, label=subtitle)

def get_userflow_setup():
    display_background_image()
    get_page_styling()
    set_title_manual(varTitle="DaddyBets", varSubtitle="User Authentication")
    cc = st.columns([1,3,1])
    with cc[1]:
        main_container = st.container(border=True, height=600)
        return main_container
        
    
def popover_menu(varPageNumber: int):
    menulist = st.popover(label="🧭 Menu", disabled=False, use_container_width=True)
    with menulist:
        st.page_link(page=get_pageconfig_item(varPageNumber=0, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=0, varPageConfigType="subtitles"), disabled=(varPageNumber == 0))
        st.page_link(page=get_pageconfig_item(varPageNumber=1, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=1, varPageConfigType="subtitles"), disabled=(varPageNumber == 1))
        st.page_link(page=get_pageconfig_item(varPageNumber=2, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=2, varPageConfigType="subtitles"), disabled=(varPageNumber == 2))
        st.page_link(page=get_pageconfig_item(varPageNumber=3, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=3, varPageConfigType="subtitles"), disabled=(varPageNumber == 3))
        st.page_link(page=get_pageconfig_item(varPageNumber=4, varPageConfigType="paths"), label=get_pageconfig_item(varPageNumber=4, varPageConfigType="subtitles"), disabled=(varPageNumber == 4))

def get_pageconfig_title_with_popmenu(varPageNumber: int, varDiv: bool=True):
    headercontainer = st.container(border=False)
    with headercontainer:
        headercols = st.columns([10,2])
        with headercols[0]:
            title = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="titles")
            subtitle = get_pageconfig_item(varPageNumber=varPageNumber, varPageConfigType="subtitles")
            st.markdown(f"""<span style="font-weight: bold; font-size: 2em; color:#7ab3ba;">{title} </span> <span style="font-weight: bold; color:#333333; font-size:1.3em;">{subtitle}</span>""", unsafe_allow_html=True)
        with headercols[1]:
            menu = popover_menu(varPageNumber=varPageNumber)
        if varDiv:
            st.divider()    


def master_page_display(varPageNumber: int):
    display_background_image()
    get_page_styling()
    #create_sidebar_nav(varPageNumber=varPageNumber)
    get_pageconfig_title(varPageNumber=varPageNumber)
    get_component_overview(varPageNumber=varPageNumber)
    if varPageNumber == 0:
        get_component_pagelinksection()

def master_page_display_styled(varPageNumber: int):
    display_background_image()
    get_page_styling()
    #create_sidebar_nav(varPageNumber=varPageNumber)
    get_pageconfig_title(varPageNumber=varPageNumber)
    #get_pageconfig_title_with_home_link(varPageNumber=varPageNumber)
    get_component_overview(varPageNumber=varPageNumber)
    if varPageNumber == 0:
        get_component_pagelinksection_styled()

def master_page_display_styled_popmenu(varPageNumber: int):
    display_background_image()
    get_page_styling()
    #create_sidebar_nav(varPageNumber=varPageNumber)
    get_pageconfig_title_with_popmenu(varPageNumber=varPageNumber)
    #get_pageconfig_title_with_home_link(varPageNumber=varPageNumber)
    get_component_overview(varPageNumber=varPageNumber)
    if varPageNumber == 0:
        get_component_pagelinksection_styled()

def master_page_display_styled_popmenu_pop(varPageNumber: int):
    display_background_image()
    get_page_styling()
    #create_sidebar_nav(varPageNumber=varPageNumber)
    get_pageconfig_title_with_popmenu(varPageNumber=varPageNumber)
    #get_pageconfig_title_with_home_link(varPageNumber=varPageNumber)
    get_component_overview(varPageNumber=varPageNumber)
    if varPageNumber == 0:
        get_component_pagelinksection_styled_popover()

def master_userflow_display():
    display_background_image2()
    get_page_styling()
    set_title_manual(varTitle="DaddyBets", varSubtitle="Welcome")
    
def container_styled(varKey: str):
    styledcontainer = sc(
        key=varKey,
        css_styles="""
            {
                border: 1px solid rgba(34, 163, 97);
                background-color: rgba(40, 94, 159, 0.5);
                border-radius: 0.5rem;
                padding: calc(1em - 1px);
                overflow: hidden; /* Prevents the content from overflowing */
                box-sizing: border-box; 
            }
            """,
    )
    return styledcontainer
#{
 #               border: 1px solid rgba(34, 163, 97);
  #              background-color: rgba(40, 94, 159, 0.5);
   #             border-radius: 0.5rem;
    #            padding: calc(1em - 1px)
     #       }    


def container_styled2(varKey):
    styledcontainer = sc(
        key=varKey,
        css_styles="""
        {
            border: 2px solid rgba(0, 0, 0, 0.2); /* Changed border color to a subtle grey */
            background-color: rgba(68, 44, 92, 0.75); /* Adjusted transparency for better visibility */
            border-radius: 0.5rem;
            padding: 1em; /* Added padding for better spacing */
            overflow: hidden; /* Keeps the content within the borders */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Soft shadow for a 3D effect */
            transition: 0.3s; /* Smooth transition for hover effects */
            box-sizing: border-box;
        }
        """
    )


    return styledcontainer

def container_styled3(varKey):
    styledcontainer = sc(
        key=varKey,
        css_styles="""
        {
            border: 2px solid rgba(0, 0, 0, 0.2); /* Changed border color to a subtle grey */
            background-color: rgba(255, 255, 255, 0.75); /* Adjusted transparency for better visibility */
            border-radius: 0.5rem;
            padding: 1em; /* Added padding for better spacing */
            overflow: hidden; /* Keeps the content within the borders */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Soft shadow for a 3D effect */
            transition: 0.3s; /* Smooth transition for hover effects */
            box-sizing: border-box;
        }
        """
    )


    return styledcontainer


def container_styled_3a(key, border=False, height=None):
    styledcontainer = sc(
        key=key,
        css_styles="""
        {
            border: 2px solid rgba(0, 0, 0, 0.2); /* Changed border color to a subtle grey */
            background-color: rgba(255, 255, 255, 0.75); /* Adjusted transparency for better visibility */
            border-radius: 0.5rem;
            padding: 1em; /* Added padding for better spacing */
            overflow: hidden; /* Keeps the content within the borders */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Soft shadow for a 3D effect */
            transition: 0.3s; /* Smooth transition for hover effects */
            box-sizing: border-box;
        }
        """
    )
    with styledcontainer:
        if height is not None:
            container = st.container(border=border, height=height)
        else:
            container = st.container(border=border)
        return container
    


def container_styled2A(key, border=False, height=None):
    styledcontainer = sc(
        key=key,
        css_styles="""
        {
            border: 2px solid rgba(0, 0, 0, 0.2); /* Changed border color to a subtle grey */
            background-color: rgba(40, 94, 159, 0.75); /* Adjusted transparency for better visibility */
            border-radius: 0.5rem;
            padding: 1em; /* Added padding for better spacing */
            overflow: hidden; /* Keeps the content within the borders */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Soft shadow for a 3D effect */
            transition: 0.3s; /* Smooth transition for hover effects */
            box-sizing: border-box;
        }
        """
    )
    with styledcontainer:
        if height is not None:
            container = st.container(border=border, height=height)
        else:
            container = st.container(border=border)
        return container




def styledexpander(varkey):
    sc = container_styled3(varKey=varkey)
    with sc:
        exp = st.expander(label="Status", expanded=True)
        with exp:
            st.write("Hey")


def switch_to_homepage():
    path = "pages/1_🏠_Home.py"
    st.switch_page(page=path)

