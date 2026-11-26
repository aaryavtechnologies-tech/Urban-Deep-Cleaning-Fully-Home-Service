import os

mapping = [
    ('floors', 'Mirror-Polished Granite Staircase', 'Deep scrubbed and buffed black granite stairs'),
    ('kitchen', 'L-Shaped Modular Kitchen Counters', 'Spotless black quartz countertop and overhead cabinets'),
    ('kitchen', 'Pristine Kitchen Platform & Storage', 'Degreased tiles, drawers and surface polishing'),
    ('floors', 'Mirror-Finish Polished Floor', 'High-gloss scrubbing and reflective floor restoration'),
    ('living', 'Sanitized Living Room Vitrified Tiles', 'Thorough floor scrubbing and skirting dusting'),
    ('wardrobes', 'Master Bedroom Mirrored Wardrobe', 'External laminate wipe-down and streak-free mirror shine'),
    ('floors', 'Deep Cleaned Utility Area & Dark Tiles', 'Tile descaling and grout scrubbing'),
    ('living', 'Bedroom Bay Windows & Wooden Flooring', 'Detailed window grill dusting and floor polish'),
    ('living', 'Bed Frame & Hardwood Floor Cleaning', 'Under-bed dust removal and wood conditioning'),
    ('living', 'Sunlit Bedroom Handover Cleaning', 'Window glass shine and dust-free interior finish'),
    ('living', 'Accent Wall & Balcony Access Area', 'Panel wipe-down and floor perimeter sanitization'),
    ('living', 'Balcony Glass Sliding Doors', 'Track vacuuming and spotless glass panel shine'),
    ('living', 'Balcony Deck & Safety Grills', 'Exterior balcony floor wash and rail dusting'),
    ('living', 'Upholstered Headboard & Bedroom Floor', 'Fabric dusting and bedside ledge sanitization'),
    ('wardrobes', 'Polished Wood Passage Door', 'Door frame degreasing and hardware shine'),
    ('living', 'Low Platform Bed & Skirting Cleaning', 'Edge-to-edge floor scrub and ledge wipe-down'),
    ('living', 'Platform Bed Frame & Parquet Flooring', 'Spotless handover preparation for master suite'),
    ('living', 'Cleaned Bedroom Layout with Wooden Flooring', 'Thorough dust extraction and surface polishing'),
    ('living', 'Bed Unit & Ambient Window Wall', 'Comprehensive bedroom deep sanitization'),
    ('wardrobes', 'Wardrobe Interior Shelves & Drawers', 'Internal vacuuming and dust-free shelf wipe'),
    ('wardrobes', 'Multi-Compartment Wardrobe Shelves', 'Sanitized linen storage and drawer tracks'),
    ('wardrobes', 'Floor-to-Ceiling Storage Unit', 'Clean interior dividers and polished wooden veneer'),
    ('wardrobes', 'Corner Wardrobe with Full-Length Mirror', 'Mirror polishing and laminate surface care'),
    ('floors', 'Polished Hardwood Bedroom Floor', 'Deep machine scrubbing and buffed finish'),
    ('bathroom', 'Chrome Rain Showerhead & Tiled Wall', 'Limescale descaling and hard water stain removal'),
    ('bathroom', 'Vanity Countertop Sink & Open Cabinet', 'Under-sink sanitization and ceramic basin descaling'),
    ('bathroom', 'Anti-Skid Bathroom Floor Tiles', 'Deep grout scrubbing and surface disinfection'),
    ('kitchen', 'Stainless Steel Kitchen Sink & Faucet', 'Scale removal, drain sanitization and chrome shine'),
    ('living', 'Detailed Switchboard & Outlet Cleaning', 'Precision grime removal from switches and sockets'),
    ('kitchen', 'Modular Kitchen Overview & Breakfast Counter', 'Complete kitchen handover deep clean'),
    ('kitchen', 'Upper Crockery Cabinets & Backsplash Tiles', 'Internal shelf disinfection and tile degreasing'),
    ('kitchen', 'Built-in Microwave & Wall Unit', 'Exterior and interior microwave sanitization'),
    ('kitchen', 'Upper Cabinet Interior Sanitization', 'Food-safe interior wipe and shelf dusting'),
    ('kitchen', 'Built-in Oven Interior Degreasing', 'Heavy-duty baking rack cleaning and glass door shine'),
    ('kitchen', 'Built-in Microwave Cavity Cleaning', 'High-heat grime extraction and interior polish'),
    ('kitchen', 'Built-in Oven Deep Cleaning & Door Care', 'Oven tray scrubbing and control panel wipe'),
    ('kitchen', 'Wide Kitchen Under-Counter Drawer', 'Cutlery drawer vacuuming and internal shelf wipe'),
    ('kitchen', 'Corner Shelf Storage & Dark Countertop', 'Blind corner cabinet cleaning and dust removal'),
    ('kitchen', 'Modular Cutlery Organizer Drawer', 'Tray extraction, wash and realignment'),
    ('kitchen', 'Pull-Out Pantry Wire Basket Cleaning', 'Slider track lubrication and basket wipe'),
    ('kitchen', 'Modular Kitchen Layout with Built-in Oven', 'Spotless kitchen finish and floor polish'),
    ('kitchen', 'Corner Platform & Sink Unit', 'Countertop polishing and backsplash tile scrub'),
    ('kitchen', 'Deep Kitchen Drawer Interior', 'Base drawer wipe and crumb extraction'),
    ('kitchen', 'Modular Chimney & Gas Hob Platform', 'Chimney exterior and cooktop burner area degreasing'),
    ('kitchen', 'Lower Cabinet Storage & Gas Connection Bay', 'Dust extraction and safety compartment wipe'),
    ('kitchen', 'Glass Top Gas Stove & Under-Drawer', 'Burner plate descaling and drawer cleaning'),
    ('kitchen', 'Under-Sink Storage Cabinets & Plumbing Bay', 'Plumbing pipe wipe-down and floor base disinfection')
]

gallery_html = []
for i, (cat, title, desc) in enumerate(mapping):
    num = f'{i+1:02d}'
    fn = f'images/work-{num}.jpg'
    gallery_html.append(f'''          <div class="gallery-item" data-category="{cat}" data-full="{fn}" data-caption="{title} &bull; {desc}">
            <img src="{fn}" alt="{title}" loading="lazy" width="400" height="300">
            <div class="gallery-overlay">
              <span class="gallery-label">{title}</span>
            </div>
          </div>''')

with open('gallery_block.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(gallery_html))

print(f'Wrote {len(gallery_html)} items to gallery_block.txt')
