from typing import Dict, Any
import os
import csv
import random
from datetime import datetime, timezone
import logging
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from dataclasses import dataclass
from faker import Faker
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

Base = declarative_base()

@dataclass
class Property(Base):
    __tablename__ = 'properties'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

@dataclass
class Process(Base):
    __tablename__ = 'processes'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

@dataclass
class Perspective(Base):
    __tablename__ = 'perspectives'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)

@dataclass
class Relationship(Base):
    __tablename__ = 'relationships'
    id: int = Column(Integer, primary_key=True)
    property_id: int = Column(Integer, ForeignKey('properties.id'))
    process_id: int = Column(Integer, ForeignKey('processes.id'))
    perspective_id: int = Column(Integer, ForeignKey('perspectives.id'))
    strength: float = Column(Float)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    property = relationship("Property", foreign_keys=[property_id])
    process = relationship("Process", foreign_keys=[process_id])
    perspective = relationship("Perspective", foreign_keys=[perspective_id])

class P3IF:
    def __init__(self, db_url: str = 'sqlite:///p3if.db', log_level: int = logging.INFO):
        self.db_url = db_url
        self.engine = create_engine(db_url)
        self.logger = self._setup_logger(log_level)
        self._recreate_database()
        self.Session = sessionmaker(bind=self.engine)
        self.faker = Faker()
        self.export_folder = 'P3IF_export'
        ensure_output_folder_exists(self.export_folder)

    def _setup_logger(self, log_level: int) -> logging.Logger:
        logger = logging.getLogger('P3IF')
        logger.setLevel(log_level)
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def _recreate_database(self):
        db_path = self.db_url.replace('sqlite:///', '')
        if os.path.exists(db_path):
            os.remove(db_path)
            self.logger.info(f"Removed existing database file: {db_path}")
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.logger.info("Database recreated successfully")

    def generate_synthetic_data(self, num_properties: int, num_processes: int, num_perspectives: int, num_relationships: int):
        session = self.Session()
        try:
            for _ in range(num_properties):
                property = Property(name=self.faker.word())
                session.add(property)
            for _ in range(num_processes):
                process = Process(name=self.faker.word())
                session.add(process)
            for _ in range(num_perspectives):
                perspective = Perspective(name=self.faker.word())
                session.add(perspective)
            session.commit()

            properties = session.query(Property).all()
            processes = session.query(Process).all()
            perspectives = session.query(Perspective).all()

            for _ in range(num_relationships):
                relationship = Relationship(
                    property=random.choice(properties).id,
                    process=random.choice(processes).id,
                    perspective=random.choice(perspectives).id,
                    strength=random.uniform(0, 1)
                )
                session.add(relationship)
            session.commit()
        except Exception as e:
            self.logger.error(f"Error generating synthetic data: {str(e)}")
            session.rollback()
        finally:
            session.close()

    def get_summary_statistics(self) -> Dict[str, Any]:
        session = self.Session()
        try:
            total_properties = session.query(Property).count()
            total_processes = session.query(Process).count()
            total_perspectives = session.query(Perspective).count()
            total_relationships = session.query(Relationship).count()
            return {
                "total_properties": total_properties,
                "total_processes": total_processes,
                "total_perspectives": total_perspectives,
                "total_relationships": total_relationships
            }
        except Exception as e:
            self.logger.error(f"Error getting summary statistics: {str(e)}")
            return {}
        finally:
            session.close()

    def visualize_relationships(self, output_folder: str):
        session = self.Session()
        try:
            relationships = pd.read_sql(session.query(Relationship).statement, self.engine)
            properties = pd.read_sql(session.query(Property).statement, self.engine)
            processes = pd.read_sql(session.query(Process).statement, self.engine)
            perspectives = pd.read_sql(session.query(Perspective).statement, self.engine)

            relationships = relationships.merge(properties, left_on='property_id', right_on='id', suffixes=('', '_property'))
            relationships = relationships.merge(processes, left_on='process_id', right_on='id', suffixes=('', '_process'))
            relationships = relationships.merge(perspectives, left_on='perspective_id', right_on='id', suffixes=('', '_perspective'))

            # Word cloud for properties
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(relationships['name_property']))
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            wordcloud_file_path = os.path.join(output_folder, "properties_wordcloud.png")
            plt.savefig(wordcloud_file_path)
            plt.close()
            self.logger.info(f"Properties word cloud saved to {wordcloud_file_path}")

            # Bar plot for properties
            plt.figure(figsize=(12, 8))
            properties_series = pd.Series(relationships['name_property'])
            sns.countplot(y=properties_series, order=properties_series.value_counts().index)
            plt.title('Count of Properties')
            plt.xlabel('Count')
            plt.ylabel('Property')
            properties_plot_path = os.path.join(output_folder, "properties_countplot.png")
            plt.savefig(properties_plot_path)
            plt.close()
            self.logger.info(f"Count plot of properties saved to {properties_plot_path}")

            # Bar plot for processes
            plt.figure(figsize=(12, 8))
            processes_series = pd.Series(relationships['name_process'])
            sns.countplot(y=processes_series, order=processes_series.value_counts().index)
            plt.title('Count of Processes')
            plt.xlabel('Count')
            plt.ylabel('Process')
            processes_plot_path = os.path.join(output_folder, "processes_countplot.png")
            plt.savefig(processes_plot_path)
            plt.close()
            self.logger.info(f"Count plot of processes saved to {processes_plot_path}")

            # Bar plot for perspectives
            plt.figure(figsize=(12, 8))
            perspectives_series = pd.Series(relationships['name_perspective'])
            sns.countplot(y=perspectives_series, order=perspectives_series.value_counts().index)
            plt.title('Count of Perspectives')
            plt.xlabel('Count')
            plt.ylabel('Perspective')
            perspectives_plot_path = os.path.join(output_folder, "perspectives_countplot.png")
            plt.savefig(perspectives_plot_path)
            plt.close()
            self.logger.info(f"Count plot of perspectives saved to {perspectives_plot_path}")

            # Violin plot for relationship strengths
            plt.figure(figsize=(12, 8))
            sns.violinplot(x=relationships['strength'])
            plt.title('Violin Plot of Relationship Strengths')
            plt.xlabel('Strength')
            violinplot_file_path = os.path.join(output_folder, "relationship_strengths_violinplot.png")
            plt.savefig(violinplot_file_path)
            plt.close()
            self.logger.info(f"Violin plot of relationship strengths saved to {violinplot_file_path}")

            # Save all visualizations to a single PDF
            save_visualizations_to_pdf(output_folder, ["properties_wordcloud.png", "properties_countplot.png", "processes_countplot.png", 
                                                       "perspectives_countplot.png", "relationship_strengths_violinplot.png"])
            self.logger.info(f"All visualizations saved to {os.path.join(output_folder, 'P3IF_visualizations.pdf')}")

        except Exception as e:
            self.logger.error(f"Error visualizing relationships: {str(e)}")
        finally:
            session.close()

# Ensure that the output folder exists
def ensure_output_folder_exists(folder: str) -> None:
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

# Save visualizations to a single PDF file
def save_visualizations_to_pdf(output_folder: str, file_names: list) -> None:
    pdf_path = os.path.join(output_folder, "P3IF_visualizations.pdf")
    with PdfPages(pdf_path) as pdf:
        for file_name in file_names:
            file_path = os.path.join(output_folder, file_name)
            if os.path.exists(file_path):
                image = plt.imread(file_path)
                plt.figure(figsize=(12, 8))
                plt.imshow(image)
                plt.axis('off')
                pdf.savefig()
                plt.close()
