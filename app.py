import pandas as pd
import numpy as np

import streamlit as st
import altair as alt
import plotly.express as px


RTM_data=pd.read_csv('RTM_with_group_weight_wss (1) (1).csv')
gt_data=pd.read_excel('GT_DATA_122_merged_filled.xlsx')
def location_wise_data_fetcher(location):
    filtered_data_rtm=RTM_data[RTM_data['Territory']==location]
    filtered_data_gt=gt_data[gt_data['Markets']==location]
    Aggregate_gt=filtered_data_gt.groupby('Markets')[['ERP GT Sales Coverage','Market_Share','Competitor Strength','White Space Score']].mean()
    
    
    return filtered_data_rtm,filtered_data_gt,Aggregate_gt
    






c1,c2,c3,c4,c5=st.columns((1,1,1,1,1),gap='medium',border=True)  
with c1:  
    selected_region = st.selectbox("Region",
                                ('CENTRAL', 'RIFT VALLEY', 'WESTERN', 'COAST', 'LAKE',
       'NORTH EASTERN', 'NAIROBI', 'EASTERN')
                                )
regional_rtm,regional_gt,aggregate_gt,=location_wise_data_fetcher(selected_region)
# with c2:


    
    
    
    
    
    

    
    

    
with c2:
    st.metric(label='Total Sales',value=round(aggregate_gt.values[0][0],2))
with c3:
    st.metric(label='Market Share',value=round(aggregate_gt.values[0][1]*100,2))
with c4:

    st.metric(label='Competitor Strength',value=round(aggregate_gt.values[0][2]*100,2))
with c5:    
    st.metric(label='White Space',value=round(aggregate_gt.values[0][3],2))
col1,col2,col3=st.columns((1,1,1))


with col1:
    st.header('White Space Score Distribution')
    
    st.altair_chart(alt.Chart(regional_rtm).mark_bar().encode(
    alt.X('AWS',bin=True),
    y="count()",
    color=alt.Color(f'count():Q',
                             legend=None,
                             scale=alt.Scale(scheme='blues')),
            stroke=alt.value('white'),
    strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
))

with col2:
    Brand=st.selectbox('Brand',regional_gt['brand'])
    Specific=regional_gt[regional_gt['brand']=='DIRIA']
    st.altair_chart(alt.Chart(Specific).mark_bar(size=20).encode(
    x=
        'SKU_CLUSTER',
            
    y="ERP GT Sales Coverage",
    color=alt.Color(f'count():Q',
                             legend=None,
                             scale=alt.Scale(scheme='blues')),
            stroke=alt.value('black'),
    strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12 )   )





