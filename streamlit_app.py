import streamlit as st
import pandas as pd
import io

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ferry Pulse AI",
    page_icon="⛴️",
    layout="wide"
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------
st.title("⛴️ Ferry Pulse AI")
st.subheader("Short-Term Ferry Ticket Demand Forecasting")

st.write(
    "A machine learning-based system for forecasting short-term "
    "ferry ticket demand and supporting predictive decisions."
)

# ---------------------------------------------------------
# DATASET SECTION
# ---------------------------------------------------------
st.header("Dataset")

st.write(
    "Upload your ferry ticket demand CSV dataset below."
)

uploaded_file = st.file_uploader(
    "Upload ferry ticket demand dataset",
    type=["csv"],
    help="Upload a CSV file containing ferry ticket demand data."
)

# ---------------------------------------------------------
# PROCESS UPLOADED FILE
# ---------------------------------------------------------
if uploaded_file is not None:

    # File size
    file_size_mb = uploaded_file.size / (1024 * 1024)

    st.write(
        f"**File:** {uploaded_file.name}  \n"
        f"**Size:** {file_size_mb:.2f} MB"
    )

    # -----------------------------------------------------
    # SAFETY CHECK
    # -----------------------------------------------------
    if file_size_mb > 200:
        st.error(
            "The uploaded file is larger than 200 MB. "
            "Please upload a smaller CSV file."
        )
        st.stop()

    # -----------------------------------------------------
    # READ CSV
    # -----------------------------------------------------
    try:
        file_bytes = uploaded_file.getvalue()

        try:
            df = pd.read_csv(
                io.BytesIO(file_bytes),
                encoding="utf-8"
            )

        except UnicodeDecodeError:
            df = pd.read_csv(
                io.BytesIO(file_bytes),
                encoding="latin1"
            )

        # -------------------------------------------------
        # SUCCESS MESSAGE
        # -------------------------------------------------
        st.success("✅ Dataset uploaded successfully!")

        # -------------------------------------------------
        # DATASET PREVIEW
        # -------------------------------------------------
        st.subheader("📊 Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

        # -------------------------------------------------
        # DATASET INFORMATION
        # -------------------------------------------------
        st.subheader("📋 Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Number of Rows",
                f"{df.shape[0]:,}"
            )

        with col2:
            st.metric(
                "Number of Columns",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Missing Values",
                f"{df.isnull().sum().sum():,}"
            )

        # -------------------------------------------------
        # COLUMN NAMES
        # -------------------------------------------------
        st.subheader("🗂️ Dataset Columns")

        st.write(list(df.columns))

        # -------------------------------------------------
        # DATA TYPES
        # -------------------------------------------------
        st.subheader("🔍 Data Types")

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
        # DATASET STATISTICS
        # -------------------------------------------------
        st.subheader("📈 Dataset Statistics")

        numeric_df = df.select_dtypes(
            include="number"
        )

        if not numeric_df.empty:

            st.dataframe(
                numeric_df.describe().round(2),
                use_container_width=True
            )

        else:

            st.info(
                "No numerical columns were found for statistical analysis."
            )

        # -------------------------------------------------
        # MISSING VALUE ANALYSIS
        # -------------------------------------------------
        st.subheader("⚠️ Missing Value Analysis")

        missing_df = pd.DataFrame({
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values,
            "Missing Percentage": (
                df.isnull().mean().values * 100
            ).round(2)
        })

        missing_df = missing_df[
            missing_df["Missing Values"] > 0
        ]

        if not missing_df.empty:

            st.dataframe(
                missing_df,
                use_container_width=True
            )

        else:

            st.success(
                "✅ No missing values found in the dataset."
            )

        # -------------------------------------------------
        # DUPLICATE ROWS
        # -------------------------------------------------
        st.subheader("🔄 Duplicate Records")

        duplicate_count = df.duplicated().sum()

        if duplicate_count > 0:

            st.warning(
                f"Found {duplicate_count:,} duplicate rows."
            )

        else:

            st.success(
                "✅ No duplicate rows found."
            )

        # -------------------------------------------------
        # BASIC DATASET SUMMARY
        # -------------------------------------------------
        st.subheader("📌 Dataset Summary")

        st.write(
            f"""
            - **Rows:** {df.shape[0]:,}
            - **Columns:** {df.shape[1]}
            - **Numerical Columns:** {len(numeric_df.columns)}
            - **Missing Values:** {df.isnull().sum().sum():,}
            - **Duplicate Rows:** {duplicate_count:,}
            """
        )

    # -----------------------------------------------------
    # ERROR HANDLING
    # -----------------------------------------------------
    except pd.errors.EmptyDataError:

        st.error(
            "❌ The uploaded CSV file is empty."
        )

    except pd.errors.ParserError:

        st.error(
            "❌ Unable to read the CSV file. "
            "Please check that the file is a valid CSV."
        )

    except Exception as e:

        st.error(
            f"❌ An error occurred while reading the dataset: {e}"
        )

else:

    st.info(
        "📂 Please upload a CSV dataset to begin."
    )
