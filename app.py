import streamlit as st

from calculations import (
    calculate_speed,
    calculate_distance,
    calculate_time,
    calculate_lift,
    calculate_drag,
    calculate_wing_loading,
    calculate_thrust_weight_ratio,
    calculate_power_weight_ratio,
    calculate_aspect_ratio
)
from graphs import(
    plot_lift_vs_airspeed,
    plot_drag_vs_airspeed,
    plot_lift_drag_ratio
)
from aviation_data import aviation_topics
# Page configuration
st.set_page_config(
    page_title="CloudChasers",
    page_icon="✈️",
    layout="wide"
)

# Custom dashboard styling
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: #00B4D8;
    font-weight: 700;
}

h2, h3 {
    color: #F5F7FA;
}

.stMetric {
    background-color: #1B2635;
    padding: 15px;
    border-radius: 10px;
}

.stButton button {
    background-color: #00B4D8;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton button:hover {
    background-color: #008EAA;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Website title
st.title("✈️ CloudChasers")

# Sidebar navigation
st.sidebar.title("Navigation")

st.sidebar.markdown("""
<h2 style="color:#00B4D8;">
    ✈ AIR SYSTEMS
</h2>
<p style="color:#9AAFC2;">
    ENGINEERING CONTROL PANEL
</p>
<hr>
""", unsafe_allow_html=True)

st.sidebar.subheader("NAVIGATION")

page = st.sidebar.selectbox(
    "Select System",
    [
        "Home",
        "Flight Calculator",
        "Aerodynamics Calculator",
        "Performance Analysis",
        "Performance Graphs",
        "Aviation Knowledge"
    ]
)

st.sidebar.divider()

st.sidebar.caption("AIRCRAFT PERFORMANCE CALCULATOR")
st.sidebar.caption("Version 1.0 | Python + Streamlit")


# Home page

if page == "Home":

    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #101F33, #163B55);
        padding: 35px;
        border-radius: 15px;
        border-left: 6px solid #00B4D8;
    ">
        <h1 style="color: #00B4D8; font-size: 38px;">
            ✈ AIRCRAFT PERFORMANCE
        </h1>
        <h3 style="color: white;">
            ENGINEERING & ANALYSIS SYSTEM
        </h3>
        <p style="color: #C5D5E5; font-size: 16px;">
            An educational platform for exploring aircraft
            performance, aerodynamics and aviation engineering.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("SYSTEM OVERVIEW")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("CALCULATION MODULES", "3")

    with col2:
        st.metric("ENGINEERING MODULES", "2")

    with col3:
        st.metric("SYSTEM STATUS", "ONLINE")

    st.divider()

    st.subheader("AVAILABLE SYSTEMS")

    col1, col2 = st.columns(2)

    with col1:
        st.info("✈️ Flight Calculator")
        st.info("🌬️ Aerodynamics Calculator")
        st.info("📊 Performance Analysis")

    with col2:
        st.info("📈 Performance Graphs")
        st.info("📚 Aviation Knowledge")

    st.divider()

    st.caption(
        "AIRCRAFT PERFORMANCE CALCULATOR | "
        "EDUCATIONAL ENGINEERING PROJECT | VERSION 1.0"
    )

# Flight Calculator
elif page == "Flight Calculator":

    st.header("✈️ Flight Calculator")

    st.write(
        "Calculate aircraft speed, travel distance "
        "and flight duration."
    )

    st.divider()

    calculation = st.selectbox(
        "Select Calculation",
        [
            "Calculate Speed",
            "Calculate Distance",
            "Calculate Flight Duration"
        ]
    )

    st.divider()

    # SPEED CALCULATION
    if calculation == "Calculate Speed":

        st.subheader("Aircraft Speed Calculator")

        distance = st.number_input(
            "Enter Distance (km)",
            min_value=0.0,
            value=600.0
        )

        time = st.number_input(
            "Enter Time (hours)",
            min_value=0.0,
            value=2.0
        )

        if st.button("Calculate Speed"):

            try:
                speed = calculate_speed(distance, time)

                st.success(
                    f"Aircraft Speed: {speed:,.2f} km/h"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Speed represents the distance travelled "
                    "by an aircraft per unit of time."
                )

                st.info(
                    "Aircraft speed is an important parameter "
                    "in studying flight duration, range and "
                    "overall aircraft performance."
                )

                st.caption(
                    "Formula: Speed = Distance / Time"
                )

            except ValueError as error:
                st.error(str(error))

    # DISTANCE CALCULATION
    elif calculation == "Calculate Distance":

        st.subheader("Flight Distance Calculator")

        speed = st.number_input(
            "Enter Speed (km/h)",
            min_value=0.0,
            value=300.0
        )

        time = st.number_input(
            "Enter Time (hours)",
            min_value=0.0,
            value=2.0
        )

        if st.button("Calculate Distance"):

            try:
                distance = calculate_distance(speed, time)

                st.success(
                    f"Flight Distance: {distance:,.2f} km"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Distance represents the total length "
                    "of the journey travelled by an aircraft."
                )

                st.info(
                    "Distance depends on aircraft speed "
                    "and the duration of travel. It is useful "
                    "when studying aircraft range."
                )

                st.caption(
                    "Formula: Distance = Speed × Time"
                )

            except ValueError as error:
                st.error(str(error))

    # FLIGHT DURATION CALCULATION
    elif calculation == "Calculate Flight Duration":

        st.subheader("Flight Duration Calculator")

        distance = st.number_input(
            "Enter Distance (km)",
            min_value=0.0,
            value=600.0
        )

        speed = st.number_input(
            "Enter Speed (km/h)",
            min_value=0.0,
            value=300.0
        )

        if st.button("Calculate Duration"):

            try:
                duration = calculate_time(distance, speed)

                total_minutes = round(duration * 60)

                hours = total_minutes // 60
                minutes = total_minutes % 60

                st.success(
                    f"Flight Duration: {duration:.2f} hours"
                )

                st.info(
                    f"Equivalent Time: {hours} hours "
                    f"and {minutes} minutes"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Flight duration represents the time "
                    "required by an aircraft to travel "
                    "a given distance at a particular speed."
                )

                st.info(
                    "Flight duration depends on the distance "
                    "travelled and the aircraft's average speed."
                )

                st.caption(
                    "Formula: Time = Distance / Speed"
                )

            except ValueError as error:
                st.error(str(error))

# Aerodynamics Calculator
elif page == "Aerodynamics Calculator":

    st.header("✈️ Aerodynamics Calculator")

    st.write(
        "Calculate aerodynamic lift and drag forces "
        "and understand their importance in aircraft design."
    )

    st.divider()

    calculation = st.selectbox(
        "Select Calculation",
        ["Calculate Lift", "Calculate Drag"]
    )

    st.divider()

    density = st.number_input(
        "Air Density (kg/m³)",
        min_value=0.0,
        value=1.225
    )

    velocity = st.number_input(
        "Airspeed (m/s)",
        min_value=0.0,
        value=100.0
    )

    wing_area = st.number_input(
        "Wing Reference Area (m²)",
        min_value=0.0,
        value=30.0
    )

    # LIFT CALCULATION
    if calculation == "Calculate Lift":

        lift_coefficient = st.number_input(
            "Lift Coefficient (CL)",
            min_value=0.0,
            value=0.8
        )

        if st.button("Calculate Lift"):

            try:
                lift = calculate_lift(
                    density,
                    velocity,
                    wing_area,
                    lift_coefficient
                )

                st.success(
                    f"Lift Force: {lift:,.2f} N"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Lift is the aerodynamic force acting "
                    "perpendicular to the airflow. It is "
                    "primarily responsible for supporting "
                    "an aircraft during flight."
                )

                st.info(
                    "Lift depends on air density, the square "
                    "of airspeed, wing reference area and "
                    "the lift coefficient."
                )

                st.caption(
                    "Formula: Lift = ½ × Density × "
                    "Airspeed² × Wing Area × CL"
                )

            except ValueError as error:
                st.error(str(error))

    # DRAG CALCULATION
    elif calculation == "Calculate Drag":

        drag_coefficient = st.number_input(
            "Drag Coefficient (CD)",
            min_value=0.0,
            value=0.03
        )

        if st.button("Calculate Drag"):

            try:
                drag = calculate_drag(
                    density,
                    velocity,
                    wing_area,
                    drag_coefficient
                )

                st.success(
                    f"Drag Force: {drag:,.2f} N"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Drag is the aerodynamic force that acts "
                    "opposite to an aircraft's motion through "
                    "the air."
                )

                st.info(
                    "Drag depends on air density, the square "
                    "of airspeed, wing reference area and "
                    "the drag coefficient. It influences "
                    "aircraft efficiency and engine requirements."
                )

                st.caption(
                    "Formula: Drag = ½ × Density × "
                    "Airspeed² × Wing Area × CD"
                )

            except ValueError as error:
                st.error(str(error))

# Performance Analysis
elif page == "Performance Analysis":

    st.header("✈️ Aircraft Performance Analysis")

    st.write(
        "Calculate important aircraft performance parameters "
        "and understand their engineering significance."
    )

    st.divider()

    calculation = st.selectbox(
        "Select Parameter",
        [
            "Wing Loading",
            "Thrust-to-Weight Ratio",
            "Power-to-Weight Ratio",
            "Aspect Ratio"
        ]
    )

    st.divider()

    # WING LOADING
    if calculation == "Wing Loading":

        st.subheader("Wing Loading Calculator")

        weight = st.number_input(
            "Aircraft Weight (N)",
            min_value=0.0,
            value=60000.0
        )

        wing_area = st.number_input(
            "Wing Area (m²)",
            min_value=0.0,
            value=30.0
        )

        if st.button("Calculate Wing Loading"):

            try:
                result = calculate_wing_loading(
                    weight, wing_area
                )

                st.success(
                    f"Wing Loading: {result:,.2f} N/m²"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Wing loading represents the aircraft's "
                    "weight divided by its wing reference area."
                )

                st.info(
                    "Wing loading is an important aircraft "
                    "design parameter. It helps engineers "
                    "study the relationship between aircraft "
                    "weight and wing area."
                )

                st.caption(
                    "Formula: Wing Loading = Weight / Wing Area"
                )

            except ValueError as error:
                st.error(str(error))

    # THRUST-TO-WEIGHT RATIO
    elif calculation == "Thrust-to-Weight Ratio":

        st.subheader("Thrust-to-Weight Ratio Calculator")

        thrust = st.number_input(
            "Engine Thrust (N)",
            min_value=0.0,
            value=120000.0
        )

        weight = st.number_input(
            "Aircraft Weight (N)",
            min_value=0.0,
            value=60000.0
        )

        if st.button("Calculate Ratio"):

            try:
                result = calculate_thrust_weight_ratio(
                    thrust, weight
                )

                st.success(
                    f"Thrust-to-Weight Ratio: {result:.3f}"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "The thrust-to-weight ratio compares "
                    "the engine thrust produced by an aircraft "
                    "with its weight."
                )

                st.info(
                    "A higher thrust-to-weight ratio generally "
                    "indicates greater thrust available relative "
                    "to aircraft weight. It is an important "
                    "parameter in studying aircraft acceleration "
                    "and climbing performance."
                )

                st.caption(
                    "Formula: Thrust-to-Weight Ratio = Thrust / Weight"
                )

            except ValueError as error:
                st.error(str(error))

    # POWER-TO-WEIGHT RATIO
    elif calculation == "Power-to-Weight Ratio":

        st.subheader("Power-to-Weight Ratio Calculator")

        power = st.number_input(
            "Engine Power (W)",
            min_value=0.0,
            value=1500000.0
        )

        mass = st.number_input(
            "Aircraft Mass (kg)",
            min_value=0.0,
            value=6000.0
        )

        if st.button("Calculate Power-to-Weight Ratio"):

            try:
                result = calculate_power_weight_ratio(
                    power, mass
                )

                st.success(
                    f"Power-to-Weight Ratio: {result:.2f} W/kg"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Power-to-weight ratio measures the "
                    "engine power available per unit mass "
                    "of the aircraft."
                )

                st.info(
                    "This parameter helps engineers understand "
                    "the relationship between engine power "
                    "and aircraft mass. It is particularly "
                    "relevant when studying powered aircraft "
                    "performance."
                )

                st.caption(
                    "Formula: Power-to-Weight Ratio = Power / Mass"
                )

            except ValueError as error:
                st.error(str(error))

    # ASPECT RATIO
    elif calculation == "Aspect Ratio":

        st.subheader("Wing Aspect Ratio Calculator")

        wingspan = st.number_input(
            "Wingspan (m)",
            min_value=0.0,
            value=15.0
        )

        wing_area = st.number_input(
            "Wing Area (m²)",
            min_value=0.0,
            value=30.0
        )

        if st.button("Calculate Aspect Ratio"):

            try:
                result = calculate_aspect_ratio(
                    wingspan, wing_area
                )

                st.success(
                    f"Aspect Ratio: {result:.2f}"
                )

                st.subheader("Engineering Interpretation")

                st.write(
                    "Aspect ratio describes the relationship "
                    "between an aircraft's wingspan and "
                    "wing reference area."
                )

                st.info(
                    "A higher aspect ratio generally indicates "
                    "a longer and narrower wing. Wing aspect "
                    "ratio influences aerodynamic characteristics "
                    "such as induced drag."
                )

                st.caption(
                    "Formula: Aspect Ratio = Wingspan² / Wing Area"
                )

            except ValueError as error:
                st.error(str(error))

# Performance Graphs
elif page == "Performance Graphs":

    st.header("📊 Aircraft Performance Graphs")

    st.write(
        "Visualise aerodynamic performance through "
        "engineering graphs and interpretations."
    )

    st.divider()

    # INPUT PARAMETERS

    density = st.number_input(
        "Air Density (kg/m³)",
        min_value=0.0,
        value=1.225
    )

    wing_area = st.number_input(
        "Wing Area (m²)",
        min_value=0.0,
        value=30.0
    )

    lift_coefficient = st.number_input(
        "Lift Coefficient (CL)",
        min_value=0.0,
        value=0.8
    )

    drag_coefficient = st.number_input(
        "Drag Coefficient (CD)",
        min_value=0.0,
        value=0.03
    )

    st.divider()

    # GRAPH SELECTION

    graph_type = st.selectbox(
        "Select Graph",
        [
            "Lift vs Airspeed",
            "Drag vs Airspeed",
            "Lift-to-Drag Ratio"
        ]
    )

    # GENERATE GRAPH

    if st.button("Generate Graph"):

        try:

            if density <= 0 or wing_area <= 0:
                st.error(
                    "Air density and wing area must be greater than zero."
                )

            elif graph_type == "Lift vs Airspeed":

                graph = plot_lift_vs_airspeed(
                    density,
                    wing_area,
                    lift_coefficient
                )

                st.pyplot(graph)

                st.subheader("Engineering Interpretation")

                st.write(
                    "This graph illustrates the relationship "
                    "between airspeed and aerodynamic lift."
                )

                st.info(
                    "As airspeed increases, lift increases "
                    "because lift is proportional to the square "
                    "of airspeed when other parameters remain constant."
                )

                st.caption(
                    "Engineering Principle: Lift ∝ Airspeed²"
                )

            elif graph_type == "Drag vs Airspeed":

                graph = plot_drag_vs_airspeed(
                    density,
                    wing_area,
                    drag_coefficient
                )

                st.pyplot(graph)

                st.subheader("Engineering Interpretation")

                st.write(
                    "This graph illustrates how aerodynamic "
                    "drag changes with airspeed."
                )

                st.info(
                    "Drag increases with the square of airspeed "
                    "when air density, wing area and drag "
                    "coefficient remain constant."
                )

                st.caption(
                    "Engineering Principle: Drag ∝ Airspeed²"
                )

            elif graph_type == "Lift-to-Drag Ratio":

                if drag_coefficient <= 0:
                    st.error(
                        "Drag coefficient must be greater than zero."
                    )

                else:

                    graph = plot_lift_drag_ratio(
                        density,
                        wing_area,
                        lift_coefficient,
                        drag_coefficient
                    )

                    st.pyplot(graph)

                    st.subheader("Engineering Interpretation")

                    st.write(
                        "The lift-to-drag ratio compares the "
                        "aerodynamic lift produced by a wing "
                        "with the drag acting on it."
                    )

                    st.info(
                        "A higher lift-to-drag ratio generally "
                        "indicates better aerodynamic efficiency. "
                        "In this simplified model, the ratio "
                        "remains constant because the lift and "
                        "drag coefficients are fixed."
                    )

                    st.caption(
                        "Formula: Lift-to-Drag Ratio = CL / CD"
                    )

        except (ValueError, ZeroDivisionError) as error:

            st.error(
                f"Unable to generate graph: {error}"
            )

# Aviation Knowledge
elif page == "Aviation Knowledge":

    st.header("📚 Aviation Knowledge")

    st.write(
        "Explore aircraft engineering concepts, "
        "aerodynamics, engines and performance."
    )

    st.divider()

    # Check whether aviation topics are available

    if aviation_topics:

        selected_topic = st.selectbox(
            "Select a Topic",
            list(aviation_topics.keys())
        )

        # Retrieve topic information

        topic_data = aviation_topics.get(selected_topic)

        if topic_data:

            st.subheader(selected_topic)

            st.info(topic_data.get(
                "description",
                "No description available."
            ))

            st.divider()

            st.subheader("Key Engineering Concepts")

            concepts = topic_data.get("concepts", {})

            if concepts:

                for concept, explanation in concepts.items():

                    with st.expander(concept):
                        st.write(explanation)

            else:
                st.warning(
                    "No concepts are currently available for this topic."
                )

        else:
            st.error("Selected topic information could not be found.")

    else:
        st.warning("No aviation topics are currently available.")
