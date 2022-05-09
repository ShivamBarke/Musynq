import React from 'react';
import { Navbar } from '../../components/navbar/index';
import { PageContainer } from '../../components/pageContainer/index';
import { TopSection } from './topSection.jsx';

export function HomePage(props) {
    return <PageContainer>
               <TopSection>
                   <Navbar/>
               </TopSection>
           </PageContainer>
}