import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ferry Pulse AI",
    page_icon="⛴️",
    layout="wide"
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("⛴️ Ferry Pulse AI")

st.subheader("Short-Term Ferry Ticket Demand Forecasting")

st.write(
    "A machine learning-based system for forecasting short-term "
    "ferry ticket demand and supporting predictive decisions."
)

# ---------------------------------------------------------
# DATASET
# ---------------------------------------------------------
st.header("📂 Dataset")

st.write(
    "Upload your ferry ticket demand CSV dataset below."
)

uploaded_file = st.file_uploader(
    "Upload ferry ticket demand dataset",
    type=["csv"],
    max_upload_size=200,
    key="ferry_csv"
)

# ---------------------------------------------------------
# PROCESS DATASET
# ---------------------------------------------------------
if uploaded_file is not None:

    try:

        with st.spinner("Reading dataset..."):

            df = pd.read_csv(uploaded_file)

        st.success("✅ Dataset uploaded successfully!")

        # -------------------------------------------------
        # BASIC INFORMATION
        # -------------------------------------------------
        st.header("📊 Dataset Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows",
                f"{df.shape[0]:,}"
            )

        with col2:
            st.metric(
                "Columns",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Missing Values",
                f"{df.isnull().sum().sum():,}"
            )

        # -------------------------------------------------
        # PREVIEW
        # -------------------------------------------------
        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

        # -------------------------------------------------
        # COLUMNS
        # -------------------------------------------------
        st.subheader("Dataset Columns")

        st.write(
            list(df.columns)
        )

        # -------------------------------------------------
        # DATA TYPES
        # -------------------------------------------------
        st.subheader("Data Types")

        dtype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Missing Values": df.isnull().sum().values
        })

        st.dataframe(
            dtype_df,
            use_container_width=True
        )

        # -------------------------------------------------
        # STATISTICS
        # -------------------------------------------------
        st.subheader("📈 Dataset Statistics")

        numeric_df = df.select_dtypes(
            include="number"
        )

        if len(numeric_df.columns) > 0:

            st.dataframe(
                numeric_df.describe().round(2),
                use_container_width=True
            )

        else:

            st.info(
                "No numerical columns were found."
            )

        # -------------------------------------------------
        # MISSING VALUES
        # -------------------------------------------------
        st.subheader("⚠️ Missing Value Analysis")

        missing = df.isnull().sum()

        missing = missing[
            missing > 0
        ]

        if len(missing) > 0:

            missing_df = pd.DataFrame({
                "Column": missing.index,
                "Missing Values": missing.values
            })

            st.dataframe(
                missing_df,
                use_container_width=True
            )

        else:

            st.success(
                "✅ No missing values found."
            )

        # -------------------------------------------------
        # DUPLICATES
        # -------------------------------------------------
        st.subheader("🔄 Duplicate Records")

        duplicates = df.duplicated().sum()

        if duplicates > 0:

            st.warning(
                f"{duplicates:,} duplicate rows found."
            )

        else:

            st.success(
                "✅ No duplicate rows found."
            )

    except pd.errors.EmptyDataError:

        st.error(
            "❌ The uploaded CSV file is empty."
        )

    except pd.errors.ParserError:

        st.error(
            "❌ The CSV file could not be parsed. "
            "Please check that it is a valid CSV file."
        )

    except Exception as e:

        st.error(
            f"❌ Error while reading dataset: {e}"
        )

else:

    st.info(
        "📁 Please upload a CSV dataset to begin."
    )
