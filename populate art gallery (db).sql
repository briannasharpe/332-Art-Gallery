INSERT INTO Artist VALUES ('Rembrandt Harmenszoon van Rijn', '164-016-4200', 'N/A', 'Leiden, Netherlands', 413, 'Baroque');
INSERT INTO Art_work VALUES ('Rembrandt Harmenszoon van Rijn', 'The Night Watch', 'Baroque', '1642-00-00', '$3,920', 'Rijksmuseum');

INSERT INTO Artist VALUES ('Thomas Gainsborough', '172-717-8800', 'N/A', 'Sudbury, England', 231, 'Rococo');
INSERT INTO Art_work VALUES ('Thomas Gainsborough', 'The Blue Boy', 'Rococo', '1770-00-00', '$3,920', 'Huntington Library');

INSERT INTO Artist VALUES ('Georges Seurat', '185-918-9100', 'N/A', 'Paris, France', 128, 'Pointillism');
INSERT INTO Art_work VALUES ('Georges Seurat', 'A Sunday Afternoon on the Island of La Grande Jatte', 'Pointillism', '1884-00-00', '$3,920', 'Art Institute of Chicago');

INSERT INTO Artist VALUES ('Jean-François Millet', '181-418-7500', 'N/A', 'Gruchy, France', 205, 'Realism');
INSERT INTO Art_work VALUES ('Jean-François Millet', 'The Gleaners', 'Realism', '1857-00-00', '$3,920', 'Musée d Orsay');

INSERT INTO Artist VALUES ('Hokusai', '176-018-4900', 'N/A', 'Edo, Japan', 269, 'Ukiyo-e');
INSERT INTO Art_work VALUES ('Hokusai', 'The Great Wave off Kanagawa', 'Ukiyo-e', '1831-00-00', '$3,920', 'The Metropolitan Museum of Art');

INSERT INTO Artist VALUES ('Leonardo da Vinci', '141-515-1900', 'N/A', 'Florence, Italy', 567, 'Renaissance');
INSERT INTO Art_work VALUES ('Leonardo da Vinci', 'Mona Lisa', 'Renaissance', '1504-00-00', '$3,920', 'Louvre Museum');

INSERT INTO Artist VALUES ('Vincent van Gogh', '185-318-9000', 'N/A', 'Zundert, Netherlands', 166, 'Modern art');
INSERT INTO Art_work VALUES ('Vincent van Gogh', 'Sunflowers', 'Modern art', '1887-00-00', '$3,920', 'Van Gogh Museum');

INSERT INTO Customer VALUES 
	(4, '199-205-0604', 'Modern art'),
	(61, '199-211-2761', 'Ukiyo-e'),
	(12, '199-301-1212', 'Realism'),
	(94, '199-404-1294', 'Rococo'),
	(1, '199-105-2201', 'Rococo'),
	(7, '199-110-0707', 'Renaissance'),
	(88, '199-401-1488' , 'Baroque'),
	(21, '199-209-2121', 'Pointillism'),
	(99, '199-103-2699', 'Pointillism'),
	(00, '199-105-2200', 'Modern art'),
	(10, '199-110-0710', 'Renaissance'),
	(68, '199-305-0268', 'Realism');

INSERT INTO Art_shows VALUES 
	('2019-12-05, 10:00', 'Van Gogh Museum', '31-20-570-5200', 'Vincent van Gogh'),
	('2019-12-10, 11:00', 'Rijksmuseum', '31-20-674-7000', 'Rembrandt Harmenszoon van Rijn'),
	('2019-12-12, 12:00', 'Louvre Museum', '33-1-40-20-50-50', 'Leonardo da Vinci'),
	('2019-12-13, 9:00', 'Musée d Orsay', '33-1-40-49-48-14', 'Jean-François Millet'),
	('2019-12-29, 10:00', 'The Metropolitan Museum of Art', '1-212-535-7710', 'Hokusai'),
	('2020-01-05, 10:00', 'Louvre Museum', '33-1-40-20-50-50', 'Leonardo da Vinci'),
	('2020-01-07, 9:00', 'Art Institute of Chicago', '1-312-443-3600', 'Georges Seurat');
