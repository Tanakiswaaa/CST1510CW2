import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

DARK_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#e6eef3'),
    legend=dict(font=dict(color='#e6eef3'))
)

class ChartBuilder:
    @staticmethod
    def create_pie_chart(df, values_col, names_col, title="Distribution"):
        fig = px.pie(df, values=values_col, names=names_col, title=title, hole=0.3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(**DARK_LAYOUT)
        return fig

    @staticmethod
    def create_bar_chart(df, x_col, y_col, title="Bar Chart", color=None):
        fig = px.bar(df, x=x_col, y=y_col, title=title, color=color if color else None, text_auto=True)
        fig.update_layout(xaxis_title=x_col.replace('_', ' ').title(),
                          yaxis_title=y_col.replace('_', ' ').title(), **DARK_LAYOUT)
        return fig

    @staticmethod
    def create_line_chart(df, x_col, y_col, title="Trend Analysis"):
        fig = px.line(df, x=x_col, y=y_col, title=title, markers=True)
        fig.update_layout(xaxis_title=x_col.replace('_', ' ').title(),
                          yaxis_title=y_col.replace('_', ' ').title(), **DARK_LAYOUT)
        return fig

    @staticmethod
    def create_heatmap(df, title="Correlation Heatmap"):
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        if numeric_df.empty:
            return None
        corr_matrix = numeric_df.corr()
        fig = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns,
                                        colorscale='RdBu', zmid=0))
        fig.update_layout(title=title, **DARK_LAYOUT)
        return fig

    @staticmethod
    def create_gauge(value, min_val, max_val, title="Gauge Chart"):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title},
            gauge={'axis': {'range': [min_val, max_val]}, 'bar': {'color': "#7df9ff"}}))
        fig.update_layout(**DARK_LAYOUT)
        return fig
